"""Exact bounded Block-229 word comparator for #7781 only.

ROWS is the 46-row output of the original228 local cylinder completion plus
229's C2 row. This explicit finite table is compared to the original runtime
at author extraction; it does not run or accept either parent campaign.
The exact two original sources and extraction receipt are historical recovery.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True, order=True)
class State:
    word: tuple[str, ...]
    foreign: frozenset[int] = frozenset()

    def __post_init__(self) -> None:
        if any(index < 0 or index >= len(self.word) for index in self.foreign):
            raise ValueError("foreign index outside word")
        if any(self.word[index] != "T" for index in self.foreign):
            raise ValueError("foreign participant must terminate on ordinary T")

    def text(self) -> str:
        return "-".join(
            f"{symbol}_F" if index in self.foreign else symbol
            for index, symbol in enumerate(self.word)
        )


@dataclass(frozen=True, order=True)
class CompiledRow:
    source: tuple[str, ...]
    contact_mask: frozenset[int]
    name: str
    target: tuple[str, ...]
    consumes: frozenset[int]
    boundary: str
    terminal: str | None

    @property
    def support(self) -> int:
        return len(self.source)


@dataclass(frozen=True, order=True)
class Step:
    name: str
    start: int
    mask: tuple[int, ...]

# Frozen supplied comparator table; source/mask/name/target/consumes/boundary/terminal.
ROW_DATA = (
    ('HLLT', (), 'K0', 'PHTL', (), 'interior', None),
    ('HLLT', (3,), 'K0_F', 'PHTL', (3,), 'interior', None),
    ('HLTA', (), 'G_A', 'PHLA', (), 'seam', None),
    ('HLTA', (2,), 'GF_A', 'PPPS', (2,), 'seam', 'ABORT'),
    ('HLTL', (), 'K1', 'PHTL', (), 'interior', None),
    ('HLTL', (2,), 'J_K1_K1_F', 'PHTL', (2,), 'interior', None),
    ('HLTT', (), 'G_T', 'PHLT', (), 'interior', None),
    ('HLTT', (3,), 'G_T', 'PHLT', (), 'interior', None),
    ('HLTT', (2,), 'GF_T', 'PHTL', (2,), 'interior', None),
    ('HLTT', (2, 3), 'GF_T', 'PHTL', (2, 3), 'interior', None),
    ('HTLA', (), 'A', 'PPPS', (), 'seam', 'ABORT'),
    ('HTLA', (1,), 'A_F', 'PPPS', (1,), 'seam', 'ABORT'),
    ('HTLL', (), 'C2', 'PHTL', (), 'interior', None),
    ('HTLT', (), 'B', 'PHTL', (), 'interior', None),
    ('HTLT', (1,), 'B_F1', 'PHTL', (1,), 'interior', None),
    ('HTLT', (3,), 'B_F3', 'PHTL', (3,), 'interior', None),
    ('HTLT', (1, 3), 'B_F1', 'PHTL', (1, 3), 'interior', None),
    ('HTTA', (2,), 'C0_A', 'PPPS', (2,), 'seam', 'ABORT'),
    ('HTTA', (1, 2), 'C0_A', 'PPPS', (1, 2), 'seam', 'ABORT'),
    ('HTTT', (2,), 'C0_T', 'PHTL', (2,), 'interior', None),
    ('HTTT', (1, 2), 'C0_T', 'PHTL', (1, 2), 'interior', None),
    ('HTTT', (2, 3), 'C0_T', 'PHTL', (2, 3), 'interior', None),
    ('PHTA', (), 'D_A', 'HTTA', (), 'seam', None),
    ('PHTA', (2,), 'J_DF_A_D_A', 'PPPS', (2,), 'seam', 'ABORT'),
    ('PHTT', (), 'D_T', 'HTTT', (), 'interior', None),
    ('PHTT', (2,), 'J_DF_T_D_T', 'PHTL', (2,), 'interior', None),
    ('PHTT', (3,), 'D_T', 'HTTT', (), 'interior', None),
    ('PHTT', (2, 3), 'J_DF_T_D_T', 'PHTL', (2, 3), 'interior', None),
    ('RHTA', (), 'Q_A', 'RHLA', (), 'root', None),
    ('RHTA', (2,), 'QF_A', 'RPPS', (2,), 'root', 'ABORT'),
    ('RHTT', (), 'Q_T', 'RHLT', (), 'root', None),
    ('RHTT', (3,), 'Q_T', 'RHLT', (), 'root', None),
    ('RHTT', (2,), 'QF_T', 'RHTL', (2,), 'root', None),
    ('RHTT', (2, 3), 'QF_T', 'RHTL', (2, 3), 'root', None),
    ('TL', (0,), 'E_TL', 'TL', (0,), 'interior', None),
    ('TTL', (), 'M', 'TLT', (), 'interior', None),
    ('TTL', (0,), 'M', 'TLT', (), 'interior', None),
    ('TTL', (1,), 'M_F', 'TLT', (1,), 'interior', None),
    ('TTL', (0, 1), 'M_F', 'TLT', (0, 1), 'interior', None),
    ('TTTA', (2,), 'CF_A', 'TTLA', (2,), 'seam', None),
    ('TTTA', (0, 2), 'CF_A', 'TTLA', (0, 2), 'seam', None),
    ('TTTA', (1, 2), 'CF_A', 'TTLA', (1, 2), 'seam', None),
    ('TTTT', (2,), 'CF_T', 'TTLT', (2,), 'interior', None),
    ('TTTT', (0, 2), 'CF_T', 'TTLT', (0, 2), 'interior', None),
    ('TTTT', (1, 2), 'CF_T', 'TTLT', (1, 2), 'interior', None),
    ('TTTT', (2, 3), 'CF_T', 'TTLT', (2, 3), 'interior', None),
)
ROWS = tuple(CompiledRow(tuple(a),frozenset(b),c,tuple(d),frozenset(e),f,g)
             for a,b,c,d,e,f,g in ROW_DATA)

def enabled_steps(
    state: State,
    rows: tuple[CompiledRow, ...] | None = None,
) -> tuple[tuple[Step, State], ...]:
    if rows is None:
        rows = ROWS
    results: list[tuple[Step, State]] = []
    for row in rows:
        width = row.support
        for start in range(len(state.word) - width + 1):
            if state.word[start : start + width] != row.source:
                continue
            local_mask = frozenset(
                index - start
                for index in state.foreign
                if start <= index < start + width
            )
            if local_mask != row.contact_mask:
                continue
            target_word = list(state.word)
            target_word[start : start + width] = row.target
            consumed = {start + offset for offset in row.consumes}
            target_foreign = frozenset(state.foreign - consumed)
            if any(target_word[index] != "T" for index in target_foreign):
                continue
            target = State(tuple(target_word), target_foreign)
            if target == state:
                continue
            results.append(
                (
                    Step(row.name, start, tuple(sorted(local_mask))),
                    target,
                )
            )
    return tuple(sorted(set(results)))


def initial_state(n: int, contacts: Iterable[int]) -> State:
    return State(
        tuple(("R", "H", *(["T"] * n), "A")),
        frozenset(1 + contact for contact in contacts),
    )

def take(state: object, name: str, start: int, rows: tuple[object, ...] = ROWS) -> object:
    matches = tuple(
        target
        for step, target in enabled_steps(state, rows)
        if step.name == name and step.start == start
    )
    if len(matches) != 1:
        raise AssertionError(f"expected one {name}@{start} from {state.text()}")
    return matches[0]


def critical_source(n: int) -> object:
    state = initial_state(n, (3, n - 4, n - 2, n))
    state = take(state, "CF_T", n - 5)
    state = take(state, "M", n - 5)
    state = take(state, "Q_T", 0)
    return state
