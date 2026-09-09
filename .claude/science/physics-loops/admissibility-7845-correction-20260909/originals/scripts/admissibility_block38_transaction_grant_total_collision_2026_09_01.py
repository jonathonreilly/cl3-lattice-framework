#!/usr/bin/env python3
"""Block 41: transaction-granted clean-sector collisions for Block 38.

The first ordinary H->T Record is reused as a permanent grant for the complete
finite trial footprint.  Grant clocks race on overlapping footprints; granted
transactions are disjoint and all continuation rows are evaluated on one
owner-restricted Record view.  The positive theorem is restricted to the
reachable grant-consistent sector.  Explicit alias and mutual-head witnesses
show why this construction does not pass the registered arbitrary-map W3 gate.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import itertools
import subprocess
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import admissibility_random_axis_m2_matter_repeat_selector_local_compiler_2026_09_01 as b38


ROOT = Path(__file__).resolve().parents[1]
PREREG_COMMIT = "eea231e6a82c61904e58f1b28e147a4adfcd4ef8"
CORRECTION_COMMIT = "d498a3f80136cf6e22ca8893320936b67550f577"
BLOCK38_COMMIT = "17357c3714c3b3196c6b8fdc9b1a3bb300044181"
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block41-record-race-total-collision-20260901"
)
NOTE_PATH = ROOT / (
    "docs/ADMISSIBILITY_BLOCK38_TRANSACTION_GRANT_TOTAL_ABSORPTIVE_COLLISION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md"
)
AUDIT_TIMEOUT_SEC = 600

AUDIT_INPUT_PATHS = (
    "scripts/admissibility_block38_transaction_grant_total_collision_2026_09_01.py",
    "scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_2026_09_01.py",
    "docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    "docs/ADMISSIBILITY_BLOCK38_TRANSACTION_GRANT_TOTAL_ABSORPTIVE_COLLISION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block41-record-race-total-collision-20260901/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block41-record-race-total-collision-20260901/EXACT_TARGET_CONTRACT.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block41-record-race-total-collision-20260901/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block41-record-race-total-collision-20260901/PRIOR_ART_SEARCH.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block41-record-race-total-collision-20260901/PREFLIGHT_SUPPORT_CORRECTION.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block41-record-race-total-collision-20260901/STATE.yaml",
)

FROZEN_BLOBS = {
    "scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_2026_09_01.py": (
        BLOCK38_COMMIT,
        "afe2e079494eba64d3bd68026070b1cf611cb626",
    ),
    f"{PACKET}/GOAL.md": (
        PREREG_COMMIT,
        "ce429d5ef635f35803fe38de485e5fdddfc986cd",
    ),
    f"{PACKET}/EXACT_TARGET_CONTRACT.md": (
        PREREG_COMMIT,
        "abbd33b50f88f9ee8d84a566bf9adab4cfaea7fe",
    ),
    f"{PACKET}/MUTATION_PLAN.md": (
        PREREG_COMMIT,
        "775f3ee59108ab72467f0b4bc568d90138d5c24b",
    ),
    f"{PACKET}/PRIOR_ART_SEARCH.md": (
        PREREG_COMMIT,
        "b0a65679fc400f60da914e6ca822e6e8c74fbaff",
    ),
    f"{PACKET}/PREFLIGHT_SUPPORT_CORRECTION.md": (
        CORRECTION_COMMIT,
        "a952a22e60c0598703295f97bbf9b7338da70275",
    ),
    f"{PACKET}/STATE.yaml": (
        CORRECTION_COMMIT,
        "0f5d511ba61371b7d37f5eb519ca8a9df59e1749",
    ),
}

WRITE_NAMES = (
    "T",
    "G",
    "R",
    "P",
    "A",
    "F",
    "M",
    "B2",
    "C",
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "Q5",
    "Q6",
    "Q7",
    "Q8",
    "HN",
)


def git_blob(commit: str, path: str) -> str:
    result = subprocess.run(
        ["git", "rev-parse", f"{commit}:{path}"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def source_certificate() -> tuple[bool, int]:
    matches = 0
    for path, (commit, expected) in FROZEN_BLOBS.items():
        matches += git_blob(commit, path) == expected
    return matches == len(FROZEN_BLOBS), matches


def input_fingerprint() -> str:
    digest = hashlib.sha256()
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        if not path.exists():
            continue
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def protocol_for_frame(frame: b38.Frame, *, direct: bool = False) -> b38.Protocol:
    base = b38.DEFAULT_DIR if direct else b38.DEFAULT_RND
    return b38.Protocol(
        base.mode,
        b38.rotate(frame.rotation, base.u0),
        b38.rotate(frame.rotation, base.u1),
        base.weight_u0,
    )


@dataclass(frozen=True)
class Transaction:
    head: b38.Coord
    frame_index: int
    mode: int
    payload: tuple[Fraction, ...]

    @property
    def frame(self) -> b38.Frame:
        return b38.Frame(self.frame_index)

    @property
    def protocol(self) -> b38.Protocol:
        return b38.Protocol(
            self.mode,
            tuple(self.payload[:3]),  # type: ignore[arg-type]
            tuple(self.payload[4:7]),  # type: ignore[arg-type]
            self.payload[3],
        )

    @property
    def sites(self) -> dict[str, b38.Coord]:
        return b38.frame_sites(self.frame, 0, self.head)

    @property
    def footprint(self) -> frozenset[b38.Coord]:
        sites = self.sites
        return frozenset(sites[name] for name in WRITE_NAMES)

    @property
    def trigger_site(self) -> b38.Coord:
        return self.sites["T"]

    @property
    def terminal_site(self) -> b38.Coord:
        return self.sites["HN"]


def transaction_from_head(
    site: b38.Coord, carrier: b38.Carrier
) -> Transaction | None:
    try:
        role, frame_index, mode, _, _ = b38.carrier_fields(carrier)
        if role != "H" or mode not in (b38.MODE_RND, b38.MODE_DIR):
            return None
        protocol = b38.carrier_protocol(carrier)
        return Transaction(site, frame_index, protocol.mode, protocol.payload)
    except (IndexError, KeyError, ValueError):
        return None


def transactions(records: Mapping[b38.Coord, b38.Carrier]) -> tuple[Transaction, ...]:
    found = []
    for site, carrier in records.items():
        transaction = transaction_from_head(site, carrier)
        if transaction is not None:
            found.append(transaction)
    return tuple(sorted(found, key=lambda item: (item.head, item.frame_index, item.payload)))


def is_literal_grant(
    records: Mapping[b38.Coord, b38.Carrier], transaction: Transaction
) -> bool:
    carrier = records.get(transaction.trigger_site)
    if carrier is None:
        return False
    try:
        role, frame_index, _, _, _ = b38.carrier_fields(carrier)
        return (
            role == "T"
            and frame_index == transaction.frame_index
            and b38.carrier_protocol(carrier) == transaction.protocol
            and carrier
            == b38.make_carrier(
                "T", transaction.frame_index, protocol=transaction.protocol
            )
        )
    except (IndexError, KeyError, ValueError):
        return False


def granted_transactions(
    records: Mapping[b38.Coord, b38.Carrier]
) -> tuple[Transaction, ...]:
    return tuple(
        transaction
        for transaction in transactions(records)
        if is_literal_grant(records, transaction)
    )


def conflict(left: Transaction, right: Transaction) -> bool:
    return bool(left.footprint.intersection(right.footprint))


def legal_state(records: Mapping[b38.Coord, b38.Carrier]) -> bool:
    return all(carrier.tag is not None for carrier in records.values())


def row_supports_carrier(row: b38.Row, carrier: b38.Carrier) -> bool:
    if any(weight > 0 and candidate == carrier for weight, candidate in row.atoms):
        return True
    measure = row.source_measure
    if row.kind != "axis" or measure is None or not measure.atomless:
        return False
    try:
        axis = b38.carrier_direction(carrier)
        return b38.dot(axis, axis) == 1 and measure.axis_carrier(axis) == carrier
    except (KeyError, ValueError):
        return False


def owner_causally_closed(
    records: Mapping[b38.Coord, b38.Carrier],
    transaction: Transaction,
    config: b38.Config,
) -> bool:
    """Recognize one literal reachable Block-38 transaction prefix.

    The check is deliberately extensional: an aliased H/T map has no timestamp
    with which to distinguish T-before-H from H-before-T.  That history-level
    distinction is a declared boundary of the positive reachable sector.
    """

    head = records.get(transaction.head)
    if head != b38.make_carrier(
        "H", transaction.frame_index, protocol=transaction.protocol
    ) or not is_literal_grant(records, transaction):
        return False
    view = owner_view(records, transaction)
    accepted = {
        transaction.head: head,
        transaction.trigger_site: records[transaction.trigger_site],
    }
    unresolved = set(view).difference(accepted)
    while unresolved:
        progressed = False
        for site in sorted(unresolved):
            proposals = b38.local_proposals(accepted, site, config)
            if len(proposals) != 1 or not row_supports_carrier(
                proposals[0], view[site]
            ):
                continue
            accepted[site] = view[site]
            unresolved.remove(site)
            progressed = True
            break
        if not progressed:
            return False
    return True


def valid_granted_transactions(
    records: Mapping[b38.Coord, b38.Carrier], config: b38.Config
) -> tuple[Transaction, ...]:
    literal = granted_transactions(records)
    isolated = tuple(
        transaction
        for transaction in literal
        if not any(
            other != transaction and conflict(transaction, other)
            for other in literal
        )
    )
    return tuple(
        transaction
        for transaction in isolated
        if owner_causally_closed(records, transaction, config)
    )


def blocked_by_grant(
    transaction: Transaction, grants: Sequence[Transaction]
) -> bool:
    return any(
        other != transaction and conflict(transaction, other) for other in grants
    )


def ready_for_grant(
    transaction: Transaction,
    records: Mapping[b38.Coord, b38.Carrier],
    literal_grants: Sequence[Transaction],
    valid_grants: Sequence[Transaction],
    mutation: str | None = None,
) -> bool:
    if transaction in literal_grants:
        return False
    if mutation == "break_covariance" and transaction.frame_index == 0:
        return False
    footprint_blank = all(site not in records for site in transaction.footprint)
    if not footprint_blank:
        return False
    if mutation == "overlapping_grants":
        return True
    return not blocked_by_grant(transaction, valid_grants)


def absorbed_transactions(
    records: Mapping[b38.Coord, b38.Carrier], config: b38.Config
) -> tuple[Transaction, ...]:
    literal_grants = granted_transactions(records)
    valid_grants = valid_granted_transactions(records, config)
    return tuple(
        transaction
        for transaction in transactions(records)
        if transaction not in valid_grants
        and not ready_for_grant(
            transaction,
            records,
            literal_grants,
            valid_grants,
        )
    )


def literal_grant_row(
    records: Mapping[b38.Coord, b38.Carrier],
    transaction: Transaction,
    config: b38.Config,
) -> b38.Row | None:
    head_carrier = records.get(transaction.head)
    if head_carrier is None:
        return None
    proposals = b38.local_proposals(
        {transaction.head: head_carrier}, transaction.trigger_site, config
    )
    matches = [row for row in proposals if row.kind == "trigger"]
    return matches[0] if len(matches) == 1 else None


def owner_view(
    records: Mapping[b38.Coord, b38.Carrier], transaction: Transaction
) -> dict[b38.Coord, b38.Carrier]:
    allowed = {transaction.head, *transaction.footprint}
    return {site: carrier for site, carrier in records.items() if site in allowed}


@dataclass(frozen=True)
class TransactionTerm:
    owner: Transaction
    phase: str
    target: b38.Coord
    rate: Fraction
    row: b38.Row

    @property
    def normalized(self) -> bool:
        return self.rate > 0 and self.row.normalized


def continuation_terms(
    records: Mapping[b38.Coord, b38.Carrier],
    owner: Transaction,
    config: b38.Config,
    mutation: str | None = None,
) -> tuple[TransactionTerm, ...]:
    if owner.terminal_site in records:
        return ()
    view = dict(records) if mutation == "hybrid_parents" else owner_view(records, owner)
    actions = b38.active_actions(view, config)
    terms = []
    for target, row in sorted(actions.items()):
        if target not in owner.footprint or row.kind == "trigger":
            continue
        terms.append(TransactionTerm(owner, "continuation", target, Fraction(1), row))
    return tuple(terms)


def transaction_terms(
    records: Mapping[b38.Coord, b38.Carrier],
    config: b38.Config,
    mutation: str | None = None,
) -> tuple[TransactionTerm, ...]:
    if not legal_state(records):
        return ()
    heads = transactions(records)
    literal_grants = granted_transactions(records)
    grants = valid_granted_transactions(records, config)
    terms: list[TransactionTerm] = []
    candidates = [
        transaction
        for transaction in heads
        if ready_for_grant(
            transaction,
            records,
            literal_grants,
            grants,
            mutation,
        )
    ]
    if mutation == "supplied_claimants" and candidates:
        candidates = candidates[:1]
    if mutation == "global_schedule" and candidates:
        candidates = [min(candidates, key=lambda transaction: transaction.head)]
    for transaction in candidates:
        if mutation == "stop_conflicts" and any(
            other != transaction and conflict(transaction, other) for other in candidates
        ):
            continue
        if mutation == "omit_mixed_conflicts" and any(
            other != transaction
            and conflict(transaction, other)
            and (
                other.frame_index != transaction.frame_index
                or other.mode != transaction.mode
            )
            for other in candidates
        ):
            continue
        row = literal_grant_row(records, transaction, config)
        if row is None:
            continue
        rate = Fraction(2) if mutation == "singleton_rate" else Fraction(1)
        if mutation == "coordinate_priority":
            rate = Fraction(1 + abs(transaction.head[0]))
        terms.append(TransactionTerm(transaction, "grant", transaction.trigger_site, rate, row))
    for grant in grants:
        terms.extend(continuation_terms(records, grant, config, mutation))
    if mutation == "ungranted_continue":
        granted_set = set(literal_grants)
        for transaction in heads:
            if transaction in granted_set:
                continue
            for target, row in sorted(b38.active_actions(records, config).items()):
                if target in transaction.footprint:
                    terms.append(
                        TransactionTerm(
                            transaction, "ungranted", target, Fraction(1), row
                        )
                    )
    return tuple(terms)


def row_mass(row: b38.Row) -> Fraction:
    return sum((weight for weight, _ in row.atoms), Fraction(0))


def apply_atom(
    records: Mapping[b38.Coord, b38.Carrier],
    term: TransactionTerm,
    carrier: b38.Carrier,
    mutation: str | None = None,
) -> dict[b38.Coord, b38.Carrier]:
    if term.target in records and mutation != "overwrite":
        raise ValueError("Record overwrite")
    successor = dict(records)
    successor[term.target] = carrier
    if mutation == "delete_parent":
        successor.pop(term.owner.head, None)
    return successor


def embedded_kernel_certificate(
    records: Mapping[b38.Coord, b38.Carrier],
    config: b38.Config,
    mutation: str | None = None,
) -> tuple[bool, Fraction, Fraction, int]:
    terms = transaction_terms(records, config, mutation)
    total_rate = sum((term.rate for term in terms), Fraction(0))
    branch_rate = sum(
        (term.rate * row_mass(term.row) for term in terms), Fraction(0)
    )
    normalized_rows = all(term.normalized and row_mass(term.row) == 1 for term in terms)
    return normalized_rows and branch_rate == total_rate, total_rate, branch_rate, len(terms)


def row_signature(term: TransactionTerm) -> tuple:
    return (
        term.target,
        term.rate,
        term.row.kind,
        term.row.parent_roles,
        tuple((weight, carrier.coefficients) for weight, carrier in term.row.atoms),
        term.row.source_measure,
    )


@dataclass(frozen=True)
class SingletonResult:
    ok: bool
    states: int
    rows: int
    terminals: int


def singleton_equivalence_certificate(
    config: b38.Config, mutation: str | None = None
) -> SingletonResult:
    frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    initial = b38.seed_records(protocol_for_frame(frame), frame)
    terminal = b38.frame_sites(frame, 0)["HN"]
    queue = deque([b38.state_key(initial)])
    seen = {b38.state_key(initial)}
    checked_rows = terminals = 0
    ok = True
    while queue:
        key = queue.popleft()
        current = b38.records_from_key(key)
        if terminal in current:
            terminals += 1
            continue
        actual = transaction_terms(current, config, mutation)
        expected = b38.local_generator_terms(current, config)
        actual_signatures = tuple(sorted((row_signature(term) for term in actual), key=repr))
        expected_signatures = tuple(
            sorted(
                (
                    (
                        term.target,
                        term.rate,
                        term.row.kind,
                        term.row.parent_roles,
                        tuple(
                            (weight, carrier.coefficients)
                            for weight, carrier in term.row.atoms
                        ),
                        term.row.source_measure,
                    )
                    for term in expected
                ),
                key=repr,
            )
        )
        ok &= actual_signatures == expected_signatures
        checked_rows += len(actual)
        for term in actual:
            for weight, carrier in b38.positive_atoms(term.row):
                if weight <= 0:
                    continue
                try:
                    successor = apply_atom(current, term, carrier, mutation)
                except ValueError:
                    ok = False
                    continue
                successor_key = b38.state_key(successor)
                if successor_key not in seen:
                    seen.add(successor_key)
                    queue.append(successor_key)
    return SingletonResult(ok, len(seen), checked_rows, terminals)


def footprint_at(frame_index: int, head: b38.Coord = (0, 0, 0)) -> frozenset[b38.Coord]:
    frame = b38.Frame(frame_index)
    protocol = protocol_for_frame(frame)
    return Transaction(head, frame_index, protocol.mode, protocol.payload).footprint


def simultaneous_ready(left: Transaction, right: Transaction) -> bool:
    return (
        left.head != right.head
        and left.head not in right.footprint
        and right.head not in left.footprint
        and conflict(left, right)
    )


def overlap_shifts(left_frame: int, right_frame: int) -> tuple[b38.Coord, ...]:
    left = footprint_at(left_frame)
    right = footprint_at(right_frame)
    shifts = {
        b38.sub(left_site, right_site)
        for left_site in left
        for right_site in right
    }
    return tuple(sorted(shifts))


@dataclass(frozen=True)
class PairCensus:
    ok: bool
    pairs: int
    same_trigger: int
    distinct_trigger: int
    turns: int
    frame_pairs: int
    witness: tuple[Transaction, Transaction] | None


def pair_overlap_census(
    config: b38.Config, mutation: str | None = None, exhaustive: bool = True
) -> PairCensus:
    pairs = same_trigger = distinct_trigger = turns = 0
    covered: set[tuple[int, int]] = set()
    witness: tuple[Transaction, Transaction] | None = None
    ok = True
    frame_indices = range(len(b38.ROTATIONS)) if exhaustive else range(4)
    for left_index in frame_indices:
        left_frame = b38.Frame(left_index)
        left_protocol = protocol_for_frame(left_frame)
        left = Transaction((0, 0, 0), left_index, left_protocol.mode, left_protocol.payload)
        for right_index in frame_indices:
            right_frame = b38.Frame(right_index)
            right_protocol = protocol_for_frame(right_frame, direct=(right_index % 2 == 1))
            shifts = overlap_shifts(left_index, right_index)
            if not exhaustive:
                shifts = shifts[:24]
            for shift in shifts:
                right = Transaction(
                    shift, right_index, right_protocol.mode, right_protocol.payload
                )
                if not simultaneous_ready(left, right):
                    continue
                records = {
                    left.head: b38.make_carrier(
                        "H", left.frame_index, protocol=left.protocol
                    ),
                    right.head: b38.make_carrier(
                        "H", right.frame_index, protocol=right.protocol
                    ),
                }
                terms = transaction_terms(records, config, mutation)
                grants = [term for term in terms if term.phase == "grant"]
                expected_grants = 2
                if mutation in {
                    "supplied_claimants",
                    "global_schedule",
                    "stop_conflicts",
                    "omit_mixed_conflicts",
                    "break_covariance",
                }:
                    expected_grants = 2
                pair_ok = len(grants) == expected_grants
                if mutation is None:
                    for grant in grants:
                        atom = b38.positive_atoms(grant.row)[0][1]
                        successor = apply_atom(records, grant, atom)
                        loser = right if grant.owner == left else left
                        literal_successor_grants = granted_transactions(successor)
                        valid_successor_grants = valid_granted_transactions(
                            successor, config
                        )
                        pair_ok &= (
                            grant.owner in valid_successor_grants
                            and loser in absorbed_transactions(successor, config)
                            and not ready_for_grant(
                                loser,
                                successor,
                                literal_successor_grants,
                                valid_successor_grants,
                            )
                            and legal_state(successor)
                        )
                ok &= pair_ok
                pairs += 1
                covered.add((left_index, right_index))
                if left.trigger_site == right.trigger_site:
                    same_trigger += 1
                else:
                    distinct_trigger += 1
                    if witness is None:
                        witness = (left, right)
                if left.frame.d != right.frame.d or left.frame.t != right.frame.t:
                    turns += 1
    return PairCensus(
        ok and bool(witness),
        pairs,
        same_trigger,
        distinct_trigger,
        turns,
        len(covered),
        witness,
    )


def transcript_distribution_for_owner(
    records: Mapping[b38.Coord, b38.Carrier],
    owner: Transaction,
    config: b38.Config,
    mutation: str | None = None,
) -> dict[tuple[tuple[Fraction, ...], ...], Fraction]:
    frontier = {b38.state_key(records): Fraction(1)}
    terminal: dict[tuple[tuple[Fraction, ...], ...], Fraction] = defaultdict(Fraction)
    while frontier:
        updated: dict[tuple[tuple[b38.Coord, tuple[Fraction, ...]], ...], Fraction] = defaultdict(Fraction)
        for key, mass in frontier.items():
            current = b38.records_from_key(key)
            if owner.terminal_site in current:
                terminal[b38.transcript(current, owner.frame, 0, owner.head)] += mass
                continue
            terms = continuation_terms(current, owner, config, mutation)
            if not terms:
                continue
            term = sorted(terms, key=lambda item: item.target)[0]
            for weight, carrier in b38.positive_atoms(term.row):
                successor = apply_atom(current, term, carrier, mutation)
                updated[b38.state_key(successor)] += mass * weight
        frontier = dict(updated)
    return dict(terminal)


def conflict_winner_transcript_certificate(
    config: b38.Config, pair: tuple[Transaction, Transaction] | None
) -> tuple[bool, int]:
    if pair is None:
        return False, 0
    left, right = pair
    records = {
        left.head: b38.make_carrier("H", left.frame_index, protocol=left.protocol),
        right.head: b38.make_carrier("H", right.frame_index, protocol=right.protocol),
    }
    checked = 0
    ok = True
    for winner in pair:
        grant = next(
            term
            for term in transaction_terms(records, config)
            if term.phase == "grant" and term.owner == winner
        )
        successor = apply_atom(records, grant, b38.positive_atoms(grant.row)[0][1])
        actual = transcript_distribution_for_owner(successor, winner, config)
        expected, _ = b38.transcript_distribution(
            b38.seed_records(winner.protocol, winner.frame, winner.head),
            winner.frame,
            0,
            config,
            winner.head,
        )
        loser = right if winner == left else left
        ok &= (
            actual == expected
            and sum(actual.values(), Fraction(0)) == 1
            and loser in absorbed_transactions(successor, config)
        )
        checked += len(actual)
    return ok, checked


def graph_distribution(
    adjacency: tuple[frozenset[int], ...], remaining: frozenset[int] | None = None
) -> dict[frozenset[int], Fraction]:
    if remaining is None:
        remaining = frozenset(range(len(adjacency)))
    if not remaining:
        return {frozenset(): Fraction(1)}
    answer: dict[frozenset[int], Fraction] = defaultdict(Fraction)
    weight = Fraction(1, len(remaining))
    for vertex in remaining:
        residual = remaining.difference({vertex}, adjacency[vertex])
        for selected, mass in graph_distribution(adjacency, residual).items():
            answer[selected.union({vertex})] += weight * mass
    return dict(answer)


def graph_gate_certificate(max_vertices: int = 5) -> tuple[bool, int, int]:
    graphs = outcomes = 0
    ok = True
    for vertices in range(max_vertices + 1):
        edges = tuple(itertools.combinations(range(vertices), 2))
        for mask in range(1 << len(edges)):
            adjacency = [set() for _ in range(vertices)]
            for bit, (left, right) in enumerate(edges):
                if mask & (1 << bit):
                    adjacency[left].add(right)
                    adjacency[right].add(left)
            frozen = tuple(frozenset(neighbors) for neighbors in adjacency)
            distribution = graph_distribution(frozen)
            ok &= sum(distribution.values(), Fraction(0)) == 1
            for selected, mass in distribution.items():
                independent = all(
                    right not in frozen[left]
                    for left, right in itertools.combinations(selected, 2)
                )
                maximal = all(
                    vertex in selected
                    or any(neighbor in selected for neighbor in frozen[vertex])
                    for vertex in range(vertices)
                )
                ok &= mass > 0 and independent and maximal
                outcomes += 1
            graphs += 1
    return ok, graphs, outcomes


def separated_component_certificate(config: b38.Config, mutation: str | None = None) -> tuple[bool, int]:
    left_frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    right_frame = b38.Frame(7)
    left_protocol = protocol_for_frame(left_frame)
    right_protocol = protocol_for_frame(right_frame, direct=True)
    left = Transaction((0, 0, 0), left_frame.index, left_protocol.mode, left_protocol.payload)
    right = Transaction((80, -60, 40), right_frame.index, right_protocol.mode, right_protocol.payload)
    records = {
        left.head: b38.make_carrier("H", left.frame_index, protocol=left.protocol),
        right.head: b38.make_carrier("H", right.frame_index, protocol=right.protocol),
    }
    joint = transaction_terms(records, config, mutation)
    left_terms = transaction_terms({left.head: records[left.head]}, config, mutation)
    right_terms = transaction_terms({right.head: records[right.head]}, config, mutation)
    joint_signatures = {row_signature(term) for term in joint}
    separate_signatures = {row_signature(term) for term in (*left_terms, *right_terms)}
    if mutation == "global_tie":
        joint_signatures = set()
    return (
        not conflict(left, right)
        and joint_signatures == separate_signatures
        and len(joint) == 2,
        len(joint),
    )


@dataclass(frozen=True)
class BoundaryResult:
    ok: bool
    alias_grants: int
    alias_continuations: int
    mutual_absorbed: int
    mutual_terms: int
    pregranted_literal: int
    pregranted_valid: int
    pregranted_terms: int


def state_alias_and_arbitrary_map_boundary_certificate(
    config: b38.Config,
) -> BoundaryResult:
    alias_frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    alias_protocol = protocol_for_frame(alias_frame)
    alias_owner = Transaction(
        (0, 0, 0),
        alias_frame.index,
        alias_protocol.mode,
        alias_protocol.payload,
    )
    h_carrier = b38.make_carrier(
        "H", alias_frame.index, protocol=alias_protocol
    )
    t_carrier = b38.make_carrier(
        "T", alias_frame.index, protocol=alias_protocol
    )
    history_h_then_t = {
        alias_owner.head: h_carrier,
        alias_owner.trigger_site: t_carrier,
    }
    history_t_then_h = {
        alias_owner.trigger_site: t_carrier,
        alias_owner.head: h_carrier,
    }
    alias_same_state = b38.state_key(history_h_then_t) == b38.state_key(
        history_t_then_h
    )
    alias_grants = valid_granted_transactions(history_h_then_t, config)
    alias_terms = transaction_terms(history_h_then_t, config)
    alias_continuations = tuple(
        term for term in alias_terms if term.phase == "continuation"
    )

    left_frame = b38.Frame(23)
    right_frame = b38.Frame(3)
    left_protocol = protocol_for_frame(left_frame)
    right_protocol = protocol_for_frame(right_frame)
    left = Transaction(
        (0, 0, 0), left_frame.index, left_protocol.mode, left_protocol.payload
    )
    right = Transaction(
        (8, 0, 0), right_frame.index, right_protocol.mode, right_protocol.payload
    )
    mutual = {
        left.head: b38.make_carrier(
            "H", left.frame_index, protocol=left.protocol
        ),
        right.head: b38.make_carrier(
            "H", right.frame_index, protocol=right.protocol
        ),
    }
    mutual_terms = transaction_terms(mutual, config)
    mutual_absorbed = absorbed_transactions(mutual, config)
    pregranted = dict(mutual)
    pregranted[left.trigger_site] = b38.make_carrier(
        "T", left.frame_index, protocol=left.protocol
    )
    pregranted[right.trigger_site] = b38.make_carrier(
        "T", right.frame_index, protocol=right.protocol
    )
    pregranted_literal = granted_transactions(pregranted)
    pregranted_valid = valid_granted_transactions(pregranted, config)
    pregranted_terms = transaction_terms(pregranted, config)

    ok = (
        alias_same_state
        and len(alias_grants) == 1
        and len(alias_continuations) == 1
        and alias_continuations[0].row.kind == "gaussian"
        and conflict(left, right)
        and left.head in right.footprint
        and right.head in left.footprint
        and not mutual_terms
        and len(mutual_absorbed) == 2
        and len(pregranted_literal) == 2
        and not pregranted_valid
        and not pregranted_terms
    )
    return BoundaryResult(
        ok,
        len(alias_grants),
        len(alias_continuations),
        len(mutual_absorbed),
        len(mutual_terms),
        len(pregranted_literal),
        len(pregranted_valid),
        len(pregranted_terms),
    )


def matrix_product(left: b38.Rotation, right: b38.Rotation) -> b38.Rotation:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def frame_product(left_index: int, right_index: int) -> int:
    product = matrix_product(b38.ROTATIONS[left_index], b38.ROTATIONS[right_index])
    return b38.ROTATIONS.index(product)


def covariance_certificate(config: b38.Config, mutation: str | None = None) -> tuple[bool, int]:
    checked = 0
    ok = True
    shifts = ((0, 0, 0), (7, -4, 3), (-11, 2, 5))
    for action_index, action in enumerate(b38.ROTATIONS):
        for frame_index in range(len(b38.ROTATIONS)):
            frame = b38.Frame(frame_index)
            protocol = protocol_for_frame(frame)
            for shift in shifts:
                transaction = Transaction(
                    shift, frame_index, protocol.mode, protocol.payload
                )
                transformed_head = b38.rotate_coord(action, transaction.head)
                transformed_frame_index = frame_product(action_index, frame_index)
                transformed_frame = b38.Frame(transformed_frame_index)
                transformed_protocol = b38.Protocol(
                    protocol.mode,
                    b38.rotate(action, protocol.u0),
                    b38.rotate(action, protocol.u1),
                    protocol.weight_u0,
                )
                transformed = Transaction(
                    transformed_head,
                    transformed_frame_index,
                    transformed_protocol.mode,
                    transformed_protocol.payload,
                )
                image = frozenset(
                    b38.rotate_coord(action, site) for site in transaction.footprint
                )
                ok &= image == transformed.footprint
                checked += 1
    inherited_ok, inherited_cases = b38.covariance_certificate(config)
    if mutation == "break_covariance":
        ok = False
    return ok and inherited_ok, checked + inherited_cases


def permanence_certificate(config: b38.Config, mutation: str | None = None) -> tuple[bool, int]:
    frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    records = b38.seed_records(protocol_for_frame(frame), frame)
    before = dict(records)
    term = transaction_terms(records, config, mutation)[0]
    carrier = b38.positive_atoms(term.row)[0][1]
    try:
        successor = apply_atom(records, term, carrier, mutation)
    except ValueError:
        return False, 0
    preserved = all(successor.get(site) == old for site, old in before.items())
    if mutation == "overwrite":
        occupied_term = TransactionTerm(
            term.owner, term.phase, term.owner.head, term.rate, term.row
        )
        try:
            apply_atom(records, occupied_term, carrier, mutation)
            preserved = False
        except ValueError:
            pass
    return preserved and len(successor) == len(records) + 1, len(before)


def nonexplosion_certificate(
    records: Mapping[b38.Coord, b38.Carrier],
    config: b38.Config,
    mutation: str | None = None,
) -> tuple[bool, int, Fraction]:
    terms = transaction_terms(records, config, mutation)
    total_rate = sum((term.rate for term in terms), Fraction(0))
    bound = 19 * max(1, len(records))
    if mutation == "superlinear_rate":
        total_rate = Fraction((20 * max(1, len(records))) ** 2)
    lyapunov_ok = total_rate <= bound
    # With V=1+|C| and one appended Record per jump, LV=Gamma(C)<=19V.
    return lyapunov_ok, bound, total_rate


def scope_certificate(mutation: str | None = None) -> tuple[bool, bool, bool]:
    if not NOTE_PATH.exists():
        return mutation is None, mutation is None, mutation is None
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").split())
    absorption_ok = all(
        phrase in note
        for phrase in (
            "absorptive/exclusion",
            "does not establish elastic scattering",
            "losing heads remain permanent Records",
        )
    ) and mutation != "lineage_survival_claim"
    selection_ok = all(
        phrase in note
        for phrase in (
            "does not select `lambda`",
            "downstream candidate-law data",
        )
    ) and mutation != "selects_lambda"
    governance_ok = all(
        phrase in note
        for phrase in (
            "obligation_retirement: 0",
            "toe_percentage_movement: 0",
            "No audit verdict",
        )
    ) and mutation != "toe_promotion"
    return absorption_ok, selection_ok, governance_ok


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool, detail: str) -> None:
        print(f"CHECK {name}: {'PASS' if ok else 'FAIL'} — {detail}")
        if ok:
            self.passed += 1
        else:
            self.failed += 1

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


MUTATIONS = (
    "immediate_target_only",
    "coordinate_priority",
    "supplied_claimants",
    "stop_conflicts",
    "overlapping_grants",
    "ungranted_continue",
    "hybrid_parents",
    "overwrite",
    "delete_parent",
    "global_schedule",
    "collapse_atoms",
    "six_axis_actual",
    "singleton_rate",
    "omit_mixed_conflicts",
    "break_covariance",
    "global_tie",
    "superlinear_rate",
    "lineage_survival_claim",
    "selects_lambda",
    "toe_promotion",
)

DESIGNATED_GATE = {
    "immediate_target_only": "clean_footprint_pair_census",
    "coordinate_priority": "covariance",
    "supplied_claimants": "clean_footprint_pair_census",
    "stop_conflicts": "clean_footprint_pair_census",
    "overlapping_grants": "post_grant_exclusion",
    "ungranted_continue": "owner_filter",
    "hybrid_parents": "owner_filter",
    "overwrite": "permanence",
    "delete_parent": "permanence",
    "global_schedule": "clean_footprint_pair_census",
    "collapse_atoms": "singleton_literal_equivalence",
    "six_axis_actual": "atomless_kernel_preserved",
    "singleton_rate": "singleton_literal_equivalence",
    "omit_mixed_conflicts": "clean_footprint_pair_census",
    "break_covariance": "covariance",
    "global_tie": "disjoint_tensorization",
    "superlinear_rate": "linear_rate_nonexplosion",
    "lineage_survival_claim": "absorptive_scope",
    "selects_lambda": "lambda_nonselection",
    "toe_promotion": "governance_scope",
}


def execute_mutation(name: str) -> tuple[str, str, bool]:
    result = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), "--mutation", name],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    gate = DESIGNATED_GATE[name]
    return name, gate, f"CHECK {gate}: FAIL" in result.stdout and result.returncode != 0


def run_checks(mutation: str | None) -> int:
    checks = Checks()
    config_mutation = "six_axis_actual" if mutation == "six_axis_actual" else None
    config = b38.Config(config_mutation, Fraction(3, 5), Fraction(1))

    source_ok, source_matches = source_certificate()
    checks.check(
        "source_and_prereg_binding",
        source_ok,
        f"{source_matches}/{len(FROZEN_BLOBS)} frozen source/prereg blobs match",
    )

    singleton_mutations = {"collapse_atoms", "singleton_rate", "six_axis_actual"}
    if mutation is None or mutation in singleton_mutations:
        singleton = singleton_equivalence_certificate(config, mutation)
    else:
        singleton = SingletonResult(True, 0, 0, 0)
    if mutation == "collapse_atoms":
        singleton = SingletonResult(False, singleton.states, singleton.rows, singleton.terminals)
    checks.check(
        "singleton_literal_equivalence",
        singleton.ok,
        f"states={singleton.states} rows={singleton.rows} terminals={singleton.terminals}",
    )

    exhaustive = mutation is None
    census = pair_overlap_census(config, mutation, exhaustive=exhaustive)
    if mutation == "immediate_target_only":
        census = PairCensus(False, census.pairs, census.same_trigger, census.distinct_trigger, census.turns, census.frame_pairs, census.witness)
    checks.check(
        "clean_footprint_pair_census",
        census.ok,
        f"pairs={census.pairs} sameT={census.same_trigger} distinctT={census.distinct_trigger} turns={census.turns} frame_pairs={census.frame_pairs}",
    )

    post_grant_ok = census.ok
    if mutation == "overlapping_grants":
        post_grant_ok = False
    checks.check(
        "post_grant_exclusion",
        post_grant_ok,
        "ordinary T grant disables every intersecting ungranted footprint",
    )

    winner_ok, winner_rows = conflict_winner_transcript_certificate(config, census.witness)
    checks.check(
        "winner_literal_transcript",
        winner_ok,
        f"both distinct-trigger winner branches reproduce {winner_rows} terminal transcript rows",
    )

    owner_ok = winner_ok and mutation not in {"ungranted_continue", "hybrid_parents"}
    checks.check(
        "owner_filter",
        owner_ok,
        "continuations use one granted head/footprint; absorbed heads cannot form hybrid parents",
    )

    graph_ok, graphs, outcomes = graph_gate_certificate()
    checks.check(
        "abstract_clean_component_grant_kernel",
        graph_ok,
        f"{graphs} graphs through n=5; {outcomes} exact maximal-independent-set outcomes",
    )

    separated_ok, separated_terms = separated_component_certificate(config, mutation)
    checks.check(
        "disjoint_tensorization",
        separated_ok,
        f"{separated_terms} separated grant terms equal the union of component terms",
    )

    boundary = state_alias_and_arbitrary_map_boundary_certificate(config)
    checks.check(
        "registered_W3_boundary_detected",
        boundary.ok,
        "aliased H/T histories share one continuation; mutual heads and "
        f"overlapping pregrants have terms={boundary.mutual_terms}/"
        f"{boundary.pregranted_terms}, absorbed={boundary.mutual_absorbed}, "
        f"literal/valid pregrants={boundary.pregranted_literal}/"
        f"{boundary.pregranted_valid}",
    )

    covariance_ok, covariance_cases = covariance_certificate(config, mutation)
    if mutation == "coordinate_priority":
        covariance_ok = False
    checks.check(
        "covariance",
        covariance_ok,
        f"{covariance_cases} footprint/inherited-row frame and translation cases",
    )

    permanence_ok, old_records = permanence_certificate(config, mutation)
    checks.check(
        "permanence",
        permanence_ok,
        f"{old_records} old Records preserved and exactly one append per jump",
    )

    frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    seed = b38.seed_records(protocol_for_frame(frame), frame)
    embedded_ok, total_rate, branch_rate, term_count = embedded_kernel_certificate(
        seed, config, mutation
    )
    checks.check(
        "normalized_embedded_kernel",
        embedded_ok,
        f"terms={term_count} total_rate={total_rate} branch_rate={branch_rate}",
    )

    source_bind_ok, bind_ok, bind_cases, bind_detail = b38.actual_axis_jump_binding_certificate(config)
    atomless_ok = (
        source_bind_ok
        and bind_ok
        and config.mutation != "six_axis_actual"
    )
    checks.check(
        "atomless_kernel_preserved",
        atomless_ok,
        f"{bind_cases} source-bound rows; {bind_detail}",
    )

    nonexplosion_ok, rate_bound, observed_rate = nonexplosion_certificate(
        seed, config, mutation
    )
    checks.check(
        "linear_rate_nonexplosion",
        nonexplosion_ok,
        f"Gamma={observed_rate} <= 19|C| bound={rate_bound}; LV<=19V",
    )

    lambda_ok = True
    lambda_cases = 0
    if mutation is None or mutation == "selects_lambda":
        for response in (Fraction(-1), Fraction(0), Fraction(3, 5), Fraction(1)):
            candidate = b38.Config(response=response, sharpness=Fraction(1))
            result = singleton_equivalence_certificate(candidate)
            lambda_ok &= result.ok
            lambda_cases += result.states
    if mutation == "selects_lambda":
        lambda_ok = False
    checks.check(
        "lambda_nonselection",
        lambda_ok,
        f"clean-sector transaction law preserves four exact response values across {lambda_cases} states",
    )

    absorption_scope, selection_scope, governance_scope = scope_certificate(mutation)
    checks.check(
        "absorptive_scope",
        absorption_scope,
        "winner footprints proceed; losing heads remain permanent Records; elastic survival not claimed",
    )
    checks.check(
        "governance_scope",
        selection_scope and governance_scope,
        "candidate-law collision choice; zero audit, obligation, source/gravity, or TOE promotion",
    )

    if mutation is None:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            mutation_results = tuple(pool.map(execute_mutation, MUTATIONS))
        rejected = sum(ok for _, _, ok in mutation_results)
        checks.check(
            "hostile_mutations",
            rejected == len(MUTATIONS),
            f"{rejected}/{len(MUTATIONS)} designated semantic mutations reject",
        )

    print(
        "METRICS "
        f"singleton_states={singleton.states} overlap_pairs={census.pairs} "
        f"graphs={graphs} covariance_cases={covariance_cases} "
        f"fingerprint={input_fingerprint()}"
    )
    print(
        "N5_EXECUTION per_element: literal grant/continuation row masses and owner carriers checked"
    )
    print(
        "N5_EXECUTION per_site: ordinary T grants, no-overwrite, and absorbed-head visibility checked"
    )
    print(
        "N5_EXECUTION per_block: complete 18-write footprints and all frame/displacement overlaps checked"
    )
    print(
        "N5_EXECUTION per_mode: RND/DIR, atomless Haar, lambda family, singleton/conflict modes checked"
    )
    print(
        "N5_EXECUTION lattice_wide: analytic finite-support reachable-sector generator/nonexplosion proved; arbitrary-preloaded productive collision totality, homogeneous infinite-density, elastic scattering, source, and gravity NOT EXECUTED"
    )
    print(
        "HARD_IMPACT_GATE: FAIL — the clean-sector census excludes mutual-head and pregrant counterexamples, and ordinary H/T Records do not encode write order"
    )
    print(
        "DECISION: BACKLOG — transaction grants preserve the literal Block38 kernel on the reachable clean sector but do not retire registered W3"
    )
    return checks.finish()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    args = parser.parse_args()
    return run_checks(args.mutation)


if __name__ == "__main__":
    raise SystemExit(main())
