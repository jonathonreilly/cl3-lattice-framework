#!/usr/bin/env python3
"""Conditional clean transaction law; six-axis controls are not the Haar law.

Corrected original #7845. Historical campaigns and mutation claims are archived.
The public transaction entry point rejects invalid exact-rational carrier and
parameter data. This runner does not execute either helper's standalone suite.
"""
from __future__ import annotations
import hashlib
import itertools
from collections import defaultdict, deque
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path
from typing import Mapping, Sequence
import admissibility_random_axis_m2_matter_repeat_selector_local_compiler_2026_09_01 as b38

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 150
AUDIT_INPUT_PATHS = ('scripts/admissibility_block38_transaction_grant_total_collision_2026_09_01.py', 'docs/ADMISSIBILITY_BLOCK38_TRANSACTION_GRANT_TOTAL_ABSORPTIVE_COLLISION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md', 'scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_2026_09_01.py', 'scripts/admissibility_block36_specific_nn_active_cut_record_front_2026_09_01.py', 'archive/notes/docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
EXPECTED_INPUT_SHA256 = {'scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_2026_09_01.py': '16ed6c31b400862a27d5f71bb9d1cc96e4cec6126ffae225cfa49c4698df283e', 'scripts/admissibility_block36_specific_nn_active_cut_record_front_2026_09_01.py': 'f03d2476fa4bf4d9d57fb7b650c19579076a48916f49c3cd145c535dad13fbd1', 'archive/notes/docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md': 'a9791acb09cc09c0727292e3407fab382fe1a634d9b8ad1ffe9c8bccaa55f359', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/ADMISSIBILITY_BLOCK38_TRANSACTION_GRANT_TOTAL_ABSORPTIVE_COLLISION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md': '38117fb3e2ec49edd3cd12f5932ed424e879a2cb930616b1cd0485defc89db6e'}
WRITE_NAMES = ('T', 'G', 'R', 'P', 'A', 'F', 'M', 'B2', 'C', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'HN')

def valid_coord(site) -> bool:
    return isinstance(site, tuple) and len(site) == 3 and all(type(v) is int for v in site)


def rational(v) -> bool:
    return type(v) in (int, Fraction)


def bloch(v) -> bool:
    return len(v) == 3 and all(rational(x) for x in v) and b38.dot(v, v) <= 1


def valid_protocol(p: b38.Protocol) -> bool:
    return p.mode in (b38.MODE_RND, b38.MODE_DIR) and rational(p.weight_u0) and 0 <= p.weight_u0 <= 1 and bloch(p.u0) and bloch(p.u1)


def valid_carrier(c) -> bool:
    """Canonical role fields and payload, with exact rational Bloch bounds.

    This host domain is narrower than mathematical real-valued carriers.
    Preloaded valid maps need not be causally reachable.
    """
    try:
        if not isinstance(c, b38.Carrier) or not all(rational(v) for v in c.coefficients):
            return False
        role, frame, mode, selector, outcome = b38.carrier_fields(c)
        if mode not in (b38.MODE_RND, b38.MODE_DIR):
            return False
        no_selector = role in {'H', 'T', 'C'}
        if (selector is not None if no_selector else selector not in (0, 1)):
            return False
        if (outcome not in (-1, 1) if role in {'F', 'B2'} else outcome is not None):
            return False
        kw = dict(mode=mode, selector=selector, outcome=outcome)
        if role in b38.PROTOCOL_ROLES:
            p = b38.carrier_protocol(c)
            if not valid_protocol(p):
                return False
            kw['protocol'] = p
        elif role == 'F':
            axis, direction = b38.carrier_axis_direction(c)
            if b38.dot(axis, axis) != 1 or direction != b38.vec_scale(Fraction(outcome), axis):
                return False
            kw.update(axis=axis, direction=direction)
        elif role == 'M':
            axis, state = b38.carrier_axis_state(c)
            if b38.dot(axis, axis) != 1 or not bloch(state):
                return False
            kw.update(axis=axis, state=state)
        elif role in {'A', 'B2'}:
            vector = b38.carrier_direction(c)
            if b38.dot(vector, vector) != 1:
                return False
            kw['axis' if role == 'A' else 'direction'] = vector
        return c == b38.make_carrier(role, frame, **kw)
    except (AttributeError, IndexError, KeyError, TypeError, ValueError):
        return False


def validate_domain(records, config) -> None:
    if not legal_state(records):
        raise ValueError('invalid exact-rational Record map')
    if config.mutation is not None or not all(rational(v) and -1 <= v <= 1 for v in (config.response, config.sharpness)):
        raise ValueError('response/sharpness must lie in [-1,1]; production mutations excluded')


def input_fingerprint() -> str:
    digest = hashlib.sha256()
    for relative in AUDIT_INPUT_PATHS:
        digest.update(relative.encode()); digest.update(b'\0')
        digest.update((ROOT / relative).read_bytes()); digest.update(b'\0')
    return digest.hexdigest()


def source_certificate() -> bool:
    # Loaded locations and actual file bytes, never historical Git objects.
    loaded = (Path(b38.__file__).resolve(), Path(b38.PARENT.__file__).resolve())
    expected_loaded = tuple((ROOT / p).resolve() for p in AUDIT_INPUT_PATHS[2:4])
    return loaded == expected_loaded and all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in EXPECTED_INPUT_SHA256.items())


def protocol_for_frame(frame: b38.Frame, *, direct: bool=False) -> b38.Protocol:
    base = b38.DEFAULT_DIR if direct else b38.DEFAULT_RND
    return b38.Protocol(base.mode, b38.rotate(frame.rotation, base.u0), b38.rotate(frame.rotation, base.u1), base.weight_u0)

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
        return b38.Protocol(self.mode, tuple(self.payload[:3]), tuple(self.payload[4:7]), self.payload[3])

    @property
    def sites(self) -> dict[str, b38.Coord]:
        return b38.frame_sites(self.frame, 0, self.head)

    @property
    def footprint(self) -> frozenset[b38.Coord]:
        sites = self.sites
        return frozenset((sites[name] for name in WRITE_NAMES))

    @property
    def trigger_site(self) -> b38.Coord:
        return self.sites['T']

    @property
    def terminal_site(self) -> b38.Coord:
        return self.sites['HN']

def transaction_from_head(site: b38.Coord, carrier: b38.Carrier) -> Transaction | None:
    try:
        if not valid_coord(site) or not valid_carrier(carrier):
            return None
        role, frame_index, mode, _, _ = b38.carrier_fields(carrier)
        if role != 'H' or mode not in (b38.MODE_RND, b38.MODE_DIR):
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

def is_literal_grant(records: Mapping[b38.Coord, b38.Carrier], transaction: Transaction) -> bool:
    carrier = records.get(transaction.trigger_site)
    if carrier is None:
        return False
    try:
        role, frame_index, _, _, _ = b38.carrier_fields(carrier)
        return role == 'T' and frame_index == transaction.frame_index and (b38.carrier_protocol(carrier) == transaction.protocol) and (carrier == b38.make_carrier('T', transaction.frame_index, protocol=transaction.protocol))
    except (IndexError, KeyError, ValueError):
        return False

def granted_transactions(records: Mapping[b38.Coord, b38.Carrier]) -> tuple[Transaction, ...]:
    return tuple((transaction for transaction in transactions(records) if is_literal_grant(records, transaction)))

def conflict(left: Transaction, right: Transaction) -> bool:
    return bool(left.footprint.intersection(right.footprint))

def legal_state(records: Mapping[b38.Coord, b38.Carrier]) -> bool:
    return all(valid_coord(site) and valid_carrier(carrier) for site, carrier in records.items())

def row_supports_carrier(row: b38.Row, carrier: b38.Carrier) -> bool:
    if any((weight > 0 and candidate == carrier for weight, candidate in row.atoms)):
        return True
    measure = row.source_measure
    if row.kind != 'axis' or measure is None or (not measure.atomless):
        return False
    try:
        axis = b38.carrier_direction(carrier)
        return b38.dot(axis, axis) == 1 and measure.axis_carrier(axis) == carrier
    except (KeyError, ValueError):
        return False

def owner_causally_closed(records: Mapping[b38.Coord, b38.Carrier], transaction: Transaction, config: b38.Config) -> bool:
    """Recognize one literal reachable Block-38 transaction prefix.

    The check is deliberately extensional: an aliased H/T map has no timestamp
    with which to distinguish T-before-H from H-before-T.  That history-level
    distinction is a declared boundary of the positive reachable sector.
    """
    head = records.get(transaction.head)
    if head != b38.make_carrier('H', transaction.frame_index, protocol=transaction.protocol) or not is_literal_grant(records, transaction):
        return False
    view = owner_view(records, transaction)
    accepted = {transaction.head: head, transaction.trigger_site: records[transaction.trigger_site]}
    unresolved = set(view).difference(accepted)
    while unresolved:
        progressed = False
        for site in sorted(unresolved):
            proposals = b38.local_proposals(accepted, site, config)
            if len(proposals) != 1 or not row_supports_carrier(proposals[0], view[site]):
                continue
            accepted[site] = view[site]
            unresolved.remove(site)
            progressed = True
            break
        if not progressed:
            return False
    return True

def valid_granted_transactions(records: Mapping[b38.Coord, b38.Carrier], config: b38.Config) -> tuple[Transaction, ...]:
    literal = granted_transactions(records)
    isolated = tuple((transaction for transaction in literal if not any((other != transaction and conflict(transaction, other) for other in literal))))
    return tuple((transaction for transaction in isolated if owner_causally_closed(records, transaction, config)))

def blocked_by_grant(transaction: Transaction, grants: Sequence[Transaction]) -> bool:
    return any((other != transaction and conflict(transaction, other) for other in grants))

def ready_for_grant(transaction: Transaction, records: Mapping[b38.Coord, b38.Carrier], literal_grants: Sequence[Transaction], valid_grants: Sequence[Transaction]) -> bool:
    if transaction in literal_grants:
        return False
    footprint_blank = all((site not in records for site in transaction.footprint))
    if not footprint_blank:
        return False
    return not blocked_by_grant(transaction, valid_grants)

def absorbed_transactions(records: Mapping[b38.Coord, b38.Carrier], config: b38.Config) -> tuple[Transaction, ...]:
    literal_grants = granted_transactions(records)
    valid_grants = valid_granted_transactions(records, config)
    return tuple((transaction for transaction in transactions(records) if transaction not in valid_grants and (not ready_for_grant(transaction, records, literal_grants, valid_grants))))

def literal_grant_row(records: Mapping[b38.Coord, b38.Carrier], transaction: Transaction, config: b38.Config) -> b38.Row | None:
    head_carrier = records.get(transaction.head)
    if head_carrier is None:
        return None
    proposals = b38.local_proposals({transaction.head: head_carrier}, transaction.trigger_site, config)
    matches = [row for row in proposals if row.kind == 'trigger']
    return matches[0] if len(matches) == 1 else None

def owner_view(records: Mapping[b38.Coord, b38.Carrier], transaction: Transaction) -> dict[b38.Coord, b38.Carrier]:
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

def continuation_terms(records: Mapping[b38.Coord, b38.Carrier], owner: Transaction, config: b38.Config) -> tuple[TransactionTerm, ...]:
    if owner.terminal_site in records:
        return ()
    view = owner_view(records, owner)
    actions = b38.active_actions(view, config)
    terms = []
    for target, row in sorted(actions.items()):
        if target not in owner.footprint or row.kind == 'trigger':
            continue
        terms.append(TransactionTerm(owner, 'continuation', target, Fraction(1), row))
    return tuple(terms)

def transaction_terms(records: Mapping[b38.Coord, b38.Carrier], config: b38.Config) -> tuple[TransactionTerm, ...]:
    validate_domain(records, config)
    heads = transactions(records)
    literal_grants = granted_transactions(records)
    grants = valid_granted_transactions(records, config)
    terms: list[TransactionTerm] = []
    candidates = [transaction for transaction in heads if ready_for_grant(transaction, records, literal_grants, grants)]
    for transaction in candidates:
        row = literal_grant_row(records, transaction, config)
        if row is None:
            continue
        rate = grant_rate(transaction)
        terms.append(TransactionTerm(transaction, 'grant', transaction.trigger_site, rate, row))
    for grant in grants:
        terms.extend(continuation_terms(records, grant, config))
    return tuple(terms)

def row_mass(row: b38.Row) -> Fraction:
    return sum((weight for weight, _ in row.atoms), Fraction(0))

def apply_atom(records: Mapping[b38.Coord, b38.Carrier], term: TransactionTerm, carrier: b38.Carrier) -> dict[b38.Coord, b38.Carrier]:
    if term.target in records:
        raise ValueError('Record overwrite')
    if not legal_state(records) or not valid_carrier(carrier) or not row_supports_carrier(term.row, carrier):
        raise ValueError('unsupported or out-of-domain Record append')
    successor = dict(records)
    successor[term.target] = carrier
    return successor

def embedded_kernel_certificate(records: Mapping[b38.Coord, b38.Carrier], config: b38.Config) -> tuple[bool, Fraction, Fraction, int]:
    terms = transaction_terms(records, config)
    total_rate = sum((term.rate for term in terms), Fraction(0))
    branch_rate = sum((term.rate * row_mass(term.row) for term in terms), Fraction(0))
    normalized_rows = all((term.normalized and row_mass(term.row) == 1 for term in terms))
    return (normalized_rows and branch_rate == total_rate, total_rate, branch_rate, len(terms))

def row_signature(term: TransactionTerm) -> tuple:
    return (term.target, term.rate, term.row.kind, term.row.parent_roles, tuple(((weight, carrier.coefficients) for weight, carrier in term.row.atoms)), term.row.source_measure)

@dataclass(frozen=True)
class SingletonResult:
    ok: bool
    states: int
    rows: int
    terminals: int

def singleton_equivalence_certificate(config: b38.Config) -> SingletonResult:
    frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    initial = b38.seed_records(protocol_for_frame(frame), frame)
    terminal = b38.frame_sites(frame, 0)['HN']
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
        actual = transaction_terms(current, config)
        expected = b38.local_generator_terms(current, config)
        actual_signatures = tuple(sorted((row_signature(term) for term in actual), key=repr))
        expected_signatures = tuple(sorted(((term.target, term.rate, term.row.kind, term.row.parent_roles, tuple(((weight, carrier.coefficients) for weight, carrier in term.row.atoms)), term.row.source_measure) for term in expected), key=repr))
        ok &= actual_signatures == expected_signatures and all(t.normalized for t in actual)
        checked_rows += len(actual)
        for term in actual:
            for weight, carrier in b38.positive_atoms(term.row):
                if weight <= 0:
                    continue
                try:
                    successor = apply_atom(current, term, carrier)
                except ValueError:
                    ok = False
                    continue
                successor_key = b38.state_key(successor)
                if successor_key not in seen:
                    seen.add(successor_key)
                    queue.append(successor_key)
    return SingletonResult(ok, len(seen), checked_rows, terminals)

def footprint_at(frame_index: int, head: b38.Coord=(0, 0, 0)) -> frozenset[b38.Coord]:
    frame = b38.Frame(frame_index)
    protocol = protocol_for_frame(frame)
    return Transaction(head, frame_index, protocol.mode, protocol.payload).footprint

def simultaneous_ready(left: Transaction, right: Transaction) -> bool:
    return left.head != right.head and left.head not in right.footprint and (right.head not in left.footprint) and conflict(left, right)

def overlap_shifts(left_frame: int, right_frame: int) -> tuple[b38.Coord, ...]:
    left = footprint_at(left_frame)
    right = footprint_at(right_frame)
    shifts = {b38.sub(left_site, right_site) for left_site in left for right_site in right}
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

def pair_overlap_census(config: b38.Config, exhaustive: bool=True) -> PairCensus:
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
            right_protocol = protocol_for_frame(right_frame, direct=right_index % 2 == 1)
            shifts = overlap_shifts(left_index, right_index)
            if not exhaustive:
                shifts = shifts[:24]
            for shift in shifts:
                right = Transaction(shift, right_index, right_protocol.mode, right_protocol.payload)
                if not simultaneous_ready(left, right):
                    continue
                records = {left.head: b38.make_carrier('H', left.frame_index, protocol=left.protocol), right.head: b38.make_carrier('H', right.frame_index, protocol=right.protocol)}
                terms = transaction_terms(records, config)
                grants = [term for term in terms if term.phase == 'grant']
                expected_grants = 2
                pair_ok = len(grants) == expected_grants
                for grant in grants:
                    atom = b38.positive_atoms(grant.row)[0][1]
                    successor = apply_atom(records, grant, atom)
                    loser = right if grant.owner == left else left
                    literal_successor_grants = granted_transactions(successor)
                    valid_successor_grants = valid_granted_transactions(successor, config)
                    pair_ok &= grant.owner in valid_successor_grants and loser in absorbed_transactions(successor, config) and (not ready_for_grant(loser, successor, literal_successor_grants, valid_successor_grants)) and legal_state(successor)
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
    return PairCensus(ok and bool(witness), pairs, same_trigger, distinct_trigger, turns, len(covered), witness)

def transcript_distribution_for_owner(records: Mapping[b38.Coord, b38.Carrier], owner: Transaction, config: b38.Config) -> dict[tuple[tuple[Fraction, ...], ...], Fraction]:
    frontier = {b38.state_key(records): Fraction(1)}
    terminal: dict[tuple[tuple[Fraction, ...], ...], Fraction] = defaultdict(Fraction)
    while frontier:
        updated: dict[tuple[tuple[b38.Coord, tuple[Fraction, ...]], ...], Fraction] = defaultdict(Fraction)
        for key, mass in frontier.items():
            current = b38.records_from_key(key)
            if owner.terminal_site in current:
                terminal[b38.transcript(current, owner.frame, 0, owner.head)] += mass
                continue
            terms = continuation_terms(current, owner, config)
            if not terms:
                continue
            term = sorted(terms, key=lambda item: item.target)[0]
            for weight, carrier in b38.positive_atoms(term.row):
                successor = apply_atom(current, term, carrier)
                updated[b38.state_key(successor)] += mass * weight
        frontier = dict(updated)
    return dict(terminal)

def conflict_winner_transcript_certificate(config: b38.Config, pair: tuple[Transaction, Transaction] | None) -> tuple[bool, int]:
    if pair is None:
        return (False, 0)
    left, right = pair
    records = {left.head: b38.make_carrier('H', left.frame_index, protocol=left.protocol), right.head: b38.make_carrier('H', right.frame_index, protocol=right.protocol)}
    checked = 0
    ok = True
    for winner in pair:
        grant = next((term for term in transaction_terms(records, config) if term.phase == 'grant' and term.owner == winner))
        successor = apply_atom(records, grant, b38.positive_atoms(grant.row)[0][1])
        actual = transcript_distribution_for_owner(successor, winner, config)
        expected, _ = b38.transcript_distribution(b38.seed_records(winner.protocol, winner.frame, winner.head), winner.frame, 0, config, winner.head)
        loser = right if winner == left else left
        ok &= actual == expected and sum(actual.values(), Fraction(0)) == 1 and (loser in absorbed_transactions(successor, config))
        checked += len(actual)
    return (ok, checked)

def graph_distribution(adjacency: tuple[frozenset[int], ...], remaining: frozenset[int] | None=None) -> dict[frozenset[int], Fraction]:
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

def graph_gate_certificate(max_vertices: int=5) -> tuple[bool, int, int]:
    graphs = outcomes = 0
    ok = True
    for vertices in range(max_vertices + 1):
        edges = tuple(itertools.combinations(range(vertices), 2))
        for mask in range(1 << len(edges)):
            adjacency = [set() for _ in range(vertices)]
            for bit, (left, right) in enumerate(edges):
                if mask & 1 << bit:
                    adjacency[left].add(right)
                    adjacency[right].add(left)
            frozen = tuple((frozenset(neighbors) for neighbors in adjacency))
            distribution = graph_distribution(frozen)
            ok &= sum(distribution.values(), Fraction(0)) == 1
            for selected, mass in distribution.items():
                independent = all((right not in frozen[left] for left, right in itertools.combinations(selected, 2)))
                maximal = all((vertex in selected or any((neighbor in selected for neighbor in frozen[vertex])) for vertex in range(vertices)))
                ok &= mass > 0 and independent and maximal
                outcomes += 1
            graphs += 1
    return (ok, graphs, outcomes)

def separated_component_certificate(config: b38.Config) -> tuple[bool, int]:
    left_frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    right_frame = b38.Frame(7)
    left_protocol = protocol_for_frame(left_frame)
    right_protocol = protocol_for_frame(right_frame, direct=True)
    left = Transaction((0, 0, 0), left_frame.index, left_protocol.mode, left_protocol.payload)
    right = Transaction((80, -60, 40), right_frame.index, right_protocol.mode, right_protocol.payload)
    records = {left.head: b38.make_carrier('H', left.frame_index, protocol=left.protocol), right.head: b38.make_carrier('H', right.frame_index, protocol=right.protocol)}
    joint = transaction_terms(records, config)
    left_terms = transaction_terms({left.head: records[left.head]}, config)
    right_terms = transaction_terms({right.head: records[right.head]}, config)
    joint_signatures = {row_signature(term) for term in joint}
    separate_signatures = {row_signature(term) for term in (*left_terms, *right_terms)}
    return (not conflict(left, right) and joint_signatures == separate_signatures and (len(joint) == 2), len(joint))

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

def state_alias_and_arbitrary_map_boundary_certificate(config: b38.Config) -> BoundaryResult:
    alias_frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    alias_protocol = protocol_for_frame(alias_frame)
    alias_owner = Transaction((0, 0, 0), alias_frame.index, alias_protocol.mode, alias_protocol.payload)
    h_carrier = b38.make_carrier('H', alias_frame.index, protocol=alias_protocol)
    t_carrier = b38.make_carrier('T', alias_frame.index, protocol=alias_protocol)
    history_h_then_t = {alias_owner.head: h_carrier, alias_owner.trigger_site: t_carrier}
    history_t_then_h = {alias_owner.trigger_site: t_carrier, alias_owner.head: h_carrier}
    alias_same_state = b38.state_key(history_h_then_t) == b38.state_key(history_t_then_h)
    alias_grants = valid_granted_transactions(history_h_then_t, config)
    alias_terms = transaction_terms(history_h_then_t, config)
    alias_continuations = tuple((term for term in alias_terms if term.phase == 'continuation'))
    left_frame = b38.Frame(23)
    right_frame = b38.Frame(3)
    left_protocol = protocol_for_frame(left_frame)
    right_protocol = protocol_for_frame(right_frame)
    left = Transaction((0, 0, 0), left_frame.index, left_protocol.mode, left_protocol.payload)
    right = Transaction((8, 0, 0), right_frame.index, right_protocol.mode, right_protocol.payload)
    mutual = {left.head: b38.make_carrier('H', left.frame_index, protocol=left.protocol), right.head: b38.make_carrier('H', right.frame_index, protocol=right.protocol)}
    mutual_terms = transaction_terms(mutual, config)
    mutual_absorbed = absorbed_transactions(mutual, config)
    pregranted = dict(mutual)
    pregranted[left.trigger_site] = b38.make_carrier('T', left.frame_index, protocol=left.protocol)
    pregranted[right.trigger_site] = b38.make_carrier('T', right.frame_index, protocol=right.protocol)
    pregranted_literal = granted_transactions(pregranted)
    pregranted_valid = valid_granted_transactions(pregranted, config)
    pregranted_terms = transaction_terms(pregranted, config)
    ok = alias_same_state and len(alias_grants) == 1 and (len(alias_continuations) == 1) and (alias_continuations[0].row.kind == 'gaussian') and conflict(left, right) and (left.head in right.footprint) and (right.head in left.footprint) and (not mutual_terms) and (len(mutual_absorbed) == 2) and (len(pregranted_literal) == 2) and (not pregranted_valid) and (not pregranted_terms)
    return BoundaryResult(ok, len(alias_grants), len(alias_continuations), len(mutual_absorbed), len(mutual_terms), len(pregranted_literal), len(pregranted_valid), len(pregranted_terms))

def grant_rate(transaction: Transaction) -> Fraction:
    """Supplied unit-rate convention, independent of coordinate or frame."""
    return Fraction(1)


def rejected(call) -> bool:
    try:
        call()
    except ValueError:
        return True
    return False


def domain_controls(config: b38.Config) -> tuple[bool, int]:
    frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    p = protocol_for_frame(frame)
    invalid_protocols = (
        replace(p, weight_u0=Fraction(2)), replace(p, weight_u0=Fraction(-1)),
        replace(p, u0=(Fraction(2), Fraction(0), Fraction(0))),
        replace(p, u1=(Fraction(0), Fraction(0), Fraction(2))),
    )
    bad_carriers = [b38.make_carrier('H', frame.index, protocol=x) for x in invalid_protocols]
    bad_carriers += [
        b38.make_carrier('H', frame.index, protocol=p, selector=0),
        b38.make_carrier('R', frame.index, protocol=p),
        b38.make_carrier('G', frame.index, mode=p.mode, selector=0, outcome=1),
        b38.make_carrier('A', frame.index, mode=p.mode, selector=0, axis=b38.ZERO),
        b38.make_carrier('F', frame.index, mode=p.mode, selector=0, outcome=1, axis=b38.E_X, direction=b38.E_Z),
        b38.make_carrier('M', frame.index, mode=p.mode, selector=0, axis=b38.E_X, state=(Fraction(2), Fraction(0), Fraction(0))),
    ]
    g = b38.make_carrier('G', frame.index, mode=p.mode, selector=0)
    bad_carriers.append(b38.Carrier((*g.coefficients[:-1], Fraction(1))))
    h = b38.make_carrier('H', frame.index, protocol=p)
    bad_carriers.append(b38.Carrier((h.coefficients[0], float(h.coefficients[1]), *h.coefficients[2:])))
    checks = [not legal_state({(0, 0, 0): c}) and rejected(lambda c=c: transaction_terms({(0, 0, 0): c}, config)) for c in bad_carriers]
    checks += [transaction_from_head((0, 0, 0), c) is None for c in bad_carriers[:5]]
    seed = b38.seed_records(p, frame)
    for field in ('response', 'sharpness'):
        for value in (Fraction(-2), Fraction(2)):
            checks.append(rejected(lambda field=field, value=value: transaction_terms(seed, replace(config, **{field: value}))))
    # Endpoint and interior Bloch preparations are valid, including zero selector branches.
    for weight, response, sharpness in itertools.product((Fraction(0), Fraction(1)), repeat=3):
        c = b38.Config(response=2 * response - 1, sharpness=2 * sharpness - 1)
        protocol = replace(p, weight_u0=weight, u1=(Fraction(1, 3),) * 3)
        state = b38.seed_records(protocol, frame)
        terms = transaction_terms(state, c)
        after = apply_atom(state, terms[0], terms[0].row.atoms[0][1])
        checks.append(len(terms) == 1 and all(t.normalized for t in transaction_terms(after, c)))
    return all(checks), len(checks)


def axis_point_control(config: b38.Config) -> tuple[bool, int]:
    """Actual transaction kernel at one rational point outside the six axes."""
    frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    state = b38.seed_records(protocol_for_frame(frame), frame)
    owner = transactions(state)[0]
    sites = owner.sites
    for _ in range(18):
        if sites['Q8'] in state:
            break
        terms = [t for t in transaction_terms(state, config) if t.target != sites['A']]
        if not terms:
            return False, 0
        term = min(terms, key=lambda t: t.target)
        state = apply_atom(state, term, b38.positive_atoms(term.row)[0][1])
    axis_term = next(t for t in transaction_terms(state, config) if t.target == sites['A'])
    measure = axis_term.row.source_measure
    axis = (Fraction(3, 5), Fraction(4, 5), Fraction(0))
    if measure is None or not measure.atomless or not axis_term.normalized:
        return False, 0
    axis_carrier = measure.axis_carrier(axis)
    state = apply_atom(state, axis_term, axis_carrier)
    first = next(t for t in transaction_terms(state, config) if t.target == sites['F'])
    expected = dict(b38.first_branch_weights(owner.protocol.program(0), axis, config))
    actual = {b38.carrier_fields(c)[4]: w for w, c in first.row.atoms}
    ok = axis not in b38.AXES and expected == actual and first.normalized
    cases = 1
    for _, first_carrier in b38.positive_atoms(first.row):
        after_first = apply_atom(state, first, first_carrier)
        matter = next(t for t in transaction_terms(after_first, config) if t.target == sites['M'])
        after_matter = apply_atom(after_first, matter, matter.row.atoms[0][1])
        second = next(t for t in transaction_terms(after_matter, config) if t.target == sites['B2'])
        retained_axis, v = b38.carrier_axis_state(after_matter[sites['M']])
        expected_second = dict(b38.second_branch_weights(v, retained_axis, config))
        actual_second = {b38.carrier_fields(c)[4]: w for w, c in second.row.atoms}
        ok &= second.normalized and expected_second == actual_second and second.row.parent_roles == ('M', 'Q6')
        cases += len(actual_second)
    # Changed row data, tested by the same support/normalization predicates.
    six = replace(axis_term.row, source_measure=replace(measure, family='six_axis_control_miscast_as_actual'))
    collapsed = replace(first.row, atoms=first.row.atoms[:1])
    ok &= not row_supports_carrier(six, axis_carrier) and not collapsed.normalized
    return bool(ok), cases


def grant_control(pair, config) -> tuple[bool, str]:
    """Exercise changed conflict and rate implementations; no name-forced result."""
    global conflict, grant_rate
    left, right = pair
    state = {t.head: b38.make_carrier('H', t.frame_index, protocol=t.protocol) for t in pair}

    def exclusion_holds():
        grants = [t for t in transaction_terms(state, config) if t.phase == 'grant']
        if len(grants) != 2:
            return False
        for term in grants:
            after = apply_atom(state, term, term.row.atoms[0][1])
            if any(t.phase == 'grant' for t in transaction_terms(after, config)):
                return False
        return True

    def translation_rates():
        frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
        p = protocol_for_frame(frame)
        return tuple(tuple(t.rate for t in transaction_terms(b38.seed_records(p, frame, shift), config)) for shift in ((0, 0, 0), (7, -4, 3)))

    baseline_exclusion = exclusion_holds()
    original_conflict = conflict
    try:
        conflict = lambda a, b: a.trigger_site == b.trigger_site
        reduced_exclusion = exclusion_holds()
    finally:
        conflict = original_conflict
    baseline_rates = translation_rates()
    original_rate = grant_rate
    try:
        grant_rate = lambda t: Fraction(1 + abs(t.head[0]))
        biased_rates = translation_rates()
    finally:
        grant_rate = original_rate
    ok = baseline_exclusion and not reduced_exclusion and baseline_rates[0] == baseline_rates[1] and biased_rates[0] != biased_rates[1]
    return ok, f'exclusion full/trigger-only={baseline_exclusion}/{reduced_exclusion}; rates unit={baseline_rates}, coordinate-biased={biased_rates}'


def geometry_covariance_control() -> tuple[bool, int]:
    count = 0
    for action in b38.ROTATIONS:
        for frame in b38.ROTATIONS:
            product = tuple(tuple(sum(action[i][k] * frame[k][j] for k in range(3)) for j in range(3)) for i in range(3))
            frame_index = b38.ROTATIONS.index(frame)
            target_index = b38.ROTATIONS.index(product)
            for shift in ((0, 0, 0), (7, -4, 3), (-11, 2, 5)):
                source = footprint_at(frame_index, shift)
                target = footprint_at(target_index, b38.rotate_coord(action, shift))
                if frozenset(b38.rotate_coord(action, x) for x in source) != target:
                    return False, count
                count += 1
    return True, count


def main() -> int:
    outcomes = []

    def check(name, ok, detail):
        outcomes.append(bool(ok))
        print(f"CHECK {name}: {'PASS' if ok else 'FAIL'} — {detail}", flush=True)

    config = b38.Config(response=Fraction(3, 5), sharpness=Fraction(1))
    check('actual_source_binding', source_certificate(), 'loaded Block38/37 files and required note/memo bytes; missing files reject')
    ok, count = domain_controls(config)
    check('parameter_and_carrier_domain', ok, f'{count} actual rejection/endpoint controls')
    singleton = singleton_equivalence_certificate(config)
    check('six_axis_singleton_equivalence', singleton.ok and (singleton.states, singleton.rows, singleton.terminals) == (652, 852, 48), f'{singleton}; finite structural quotient only')
    census = pair_overlap_census(config, exhaustive=False)
    check('bounded_overlap_exclusion', census.ok, f'{census.pairs} pairs; sameT={census.same_trigger}, distinctT={census.distinct_trigger}; first 4 frames and first 24 shifts per frame pair')
    winner_ok, winner_rows = conflict_winner_transcript_certificate(config, census.witness)
    check('six_axis_winner_law', winner_ok and winner_rows == 96, f'{winner_rows} finite winner control rows, not a continuum census')
    changed_ok, changed_detail = grant_control(census.witness, config)
    check('changed_kernel_controls', changed_ok, changed_detail)
    axis_ok, axis_cases = axis_point_control(config)
    check('non_cubature_actual_transaction', axis_ok, f'{axis_cases} first/second branch entries; actual axis append; collapsed row and six-axis replacement rejected')
    graph_ok, graphs, graph_outcomes = graph_gate_certificate()
    check('fixed_finite_graph_race', graph_ok and (graphs, graph_outcomes) == (1100, 3726), f'{graphs} graphs through n=5, {graph_outcomes} exact maximal-independent-set outcomes')
    separated_ok, separated_terms = separated_component_certificate(config)
    check('separated_component_union', separated_ok, f'{separated_terms} initial grant terms')
    boundary = state_alias_and_arbitrary_map_boundary_certificate(config)
    check('valid_preloaded_boundaries', boundary.ok, repr(boundary))
    geometry_ok, geometry_count = geometry_covariance_control()
    check('footprint_covariance', geometry_ok, f'{geometry_count} rotated footprint cases; row covariance is the conditional dot-product argument in the note')
    frame = b38.Frame(b38.IDENTITY_FRAME_INDEX)
    seed = b38.seed_records(protocol_for_frame(frame), frame)
    term = transaction_terms(seed, config)[0]
    successor = apply_atom(seed, term, term.row.atoms[0][1])
    check('append_only_control', all(successor.get(k) == v for k, v in seed.items()) and len(successor) == len(seed) + 1 and rejected(lambda: apply_atom(successor, term, term.row.atoms[0][1])), 'actual duplicate target raises; all old Records preserved')
    embedded_ok, rate, branch_rate, terms = embedded_kernel_certificate(seed, config)
    check('finite_seed_mass_and_rate', embedded_ok and rate <= 19 * len(seed), f'{terms} term; rate={rate}, finite branch mass rate={branch_rate}; universal bound uses counting proof')
    print(f'INPUT_FINGERPRINT: {input_fingerprint()}')
    print('SCOPE: supplied valid-domain clean causal-prefix transaction law; finite controls plus conditional analytic measure/DAG proof; no W3 retirement, physical clock, lambda selection, or audit verdict')
    print(f'TOTAL: PASS={sum(outcomes)} FAIL={len(outcomes) - sum(outcomes)}')
    return 0 if all(outcomes) else 1


if __name__ == '__main__':
    raise SystemExit(main())
