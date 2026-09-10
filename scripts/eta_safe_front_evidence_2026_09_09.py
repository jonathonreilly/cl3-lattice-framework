"""Small source-binding and control-report helpers for corrected Eta B12--B16.

This module does not compute physics.  It keeps two evidence rules identical
across the ten finite runners: current working bytes must be the bytes that the
runner imports, and a clean unmodified baseline is required before any control
probe can count as detected.
"""

from __future__ import annotations

import ast
from collections import Counter
from dataclasses import dataclass
import hashlib
from pathlib import Path
from types import ModuleType
from typing import Callable, Mapping, Sequence


CONTROL_KINDS = (
    "changed_object",
    "assertion_guard",
    "syntax_guard",
    "scope_guard",
)


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def imported_module_names(path: Path) -> frozenset[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return frozenset(names)


def source_binding_facts(
    *,
    root: Path,
    source_path: str,
    audit_input_paths: Sequence[str],
    imported_modules: Mapping[str, ModuleType],
    forbidden_imports: Sequence[str] = (),
) -> dict[str, object]:
    """Bind imports and declared inputs to the current checkout, without Git.

    Cache identity is supplied by ``runner_cache.py`` over the same literal
    ``AUDIT_INPUT_PATHS``.  These in-run checks ensure that Python resolved each
    named module to the declared working-tree file rather than to another
    checkout or an installed copy.
    """

    source = (root / source_path).resolve()
    inputs = tuple(audit_input_paths)
    input_files = tuple((root / relative).resolve() for relative in inputs)
    expected_modules = {
        label: (root / relative).resolve()
        for label, relative in (
            (label, f"scripts/{module.__name__.split('.')[-1]}.py")
            for label, module in imported_modules.items()
        )
    }
    actual_modules = {
        label: Path(module.__file__ or "").resolve()
        for label, module in imported_modules.items()
    }
    declared_input_set = set(input_files)
    imports = imported_module_names(source)
    forbidden = tuple(
        name for name in forbidden_imports
        if name in imports or any(item.startswith(name + ".") for item in imports)
    )
    readable = all(path.is_file() for path in input_files)
    inside_root = True
    for path in (source,) + input_files + tuple(actual_modules.values()):
        try:
            path.relative_to(root.resolve())
        except ValueError:
            inside_root = False
    return {
        "source_path": source,
        "source_current": source == Path(__file__).resolve().with_name(Path(source_path).name),
        "declared_inputs": len(inputs),
        "inputs_unique": len(inputs) == len(set(inputs)),
        "inputs_readable": readable,
        "inputs_inside_root": inside_root,
        "input_sha256": tuple(
            (relative, sha256_path(path))
            for relative, path in zip(inputs, input_files)
            if path.is_file()
        ),
        "module_paths": tuple(
            (label, actual_modules[label], expected_modules[label])
            for label in sorted(actual_modules)
        ),
        "modules_current": actual_modules == expected_modules,
        "module_paths_declared": all(
            path in declared_input_set for path in expected_modules.values()
        ),
        "forbidden_imports": forbidden,
        "git_authority_used": False,
    }


def source_binding_ok(facts: Mapping[str, object]) -> bool:
    return bool(
        facts["source_current"]
        and facts["declared_inputs"]
        and facts["inputs_unique"]
        and facts["inputs_readable"]
        and facts["inputs_inside_root"]
        and facts["modules_current"]
        and facts["module_paths_declared"]
        and not facts["forbidden_imports"]
        and not facts["git_authority_used"]
    )


@dataclass(frozen=True, slots=True)
class ControlSweep:
    baseline_clean: bool
    baseline_failures: tuple[str, ...]
    detected: tuple[str, ...]
    survivors: tuple[str, ...]
    kind_totals: tuple[tuple[str, int], ...]
    kind_detected: tuple[tuple[str, int], ...]


CheckRows = Sequence[tuple[str, bool, str]]
Evaluator = Callable[[str], CheckRows]


def control_sweep(
    evaluate: Evaluator,
    mutations: Sequence[str],
    mutation_kinds: Mapping[str, str],
) -> ControlSweep:
    mutation_tuple = tuple(mutations)
    if set(mutation_tuple) != set(mutation_kinds):
        missing = sorted(set(mutation_tuple) - set(mutation_kinds))
        extra = sorted(set(mutation_kinds) - set(mutation_tuple))
        raise ValueError(f"control-kind coverage mismatch: missing={missing}; extra={extra}")
    invalid_kinds = sorted(set(mutation_kinds.values()) - set(CONTROL_KINDS))
    if invalid_kinds:
        raise ValueError(f"unknown control kinds: {invalid_kinds}")

    baseline_failures = tuple(
        name for name, ok, _detail in evaluate("") if not ok
    )
    totals = Counter(mutation_kinds.values())
    if baseline_failures:
        return ControlSweep(
            baseline_clean=False,
            baseline_failures=baseline_failures,
            detected=(),
            survivors=mutation_tuple,
            kind_totals=tuple((kind, totals[kind]) for kind in CONTROL_KINDS),
            kind_detected=tuple((kind, 0) for kind in CONTROL_KINDS),
        )

    detected: list[str] = []
    survivors: list[str] = []
    for mutation in mutation_tuple:
        rows = evaluate(mutation)
        if any(not ok for _name, ok, _detail in rows):
            detected.append(mutation)
        else:
            survivors.append(mutation)
    detected_counts = Counter(mutation_kinds[name] for name in detected)
    return ControlSweep(
        baseline_clean=True,
        baseline_failures=(),
        detected=tuple(detected),
        survivors=tuple(survivors),
        kind_totals=tuple((kind, totals[kind]) for kind in CONTROL_KINDS),
        kind_detected=tuple(
            (kind, detected_counts[kind]) for kind in CONTROL_KINDS
        ),
    )


def print_control_sweep(summary: ControlSweep) -> None:
    failures = ",".join(summary.baseline_failures) or "none"
    print(
        "MUTATION_BASELINE: "
        f"clean={str(summary.baseline_clean).lower()}; failures={failures}"
    )
    detected_by_kind = dict(summary.kind_detected)
    for kind, total in summary.kind_totals:
        print(
            f"CONTROL_KIND: {kind}; detected={detected_by_kind[kind]}/{total}"
        )
    if summary.baseline_clean:
        print(
            f"MUTATIONS: rejected={len(summary.detected)}/"
            f"{len(summary.detected) + len(summary.survivors)}"
        )
    else:
        print(
            "MUTATIONS: not_executed=clean_baseline_required; "
            f"controls={len(summary.survivors)}"
        )
    if summary.survivors and summary.baseline_clean:
        print("MUTATION_SURVIVORS:", ",".join(summary.survivors))


def control_sweep_failed(summary: ControlSweep) -> bool:
    return not summary.baseline_clean or bool(summary.survivors)
