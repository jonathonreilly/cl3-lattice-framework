#!/usr/bin/env python3
"""Corrected Block 170 finite moment, twist, and axis certificate.

The historical filename is retained for routing.  This producer reports raw
Gaussian moment matrices separately from their Hermitian parts, tests a named
finite coefficient family, and treats mass brackets, twists, and exchange maps
as finite measurements.  It is not an exhaustive audit or physical no-go.
"""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10 as h


R = sp.Rational
I = sp.I
SLICE_C = 1
HISTORICAL_BISECTION_STEPS = 7

AUDIT_INPUT_PATHS = ('scripts/admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10.py',
 'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_CLOSURE_AUDIT_TWO_BOUNDED_THEOREM_NOTE_2026-08-21.md',
 '.claude/science/physics-loops/toe-axiom-closure-block170-closure-audit-two-20260821/NO_GO_LEDGER.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/audit/data/axiom_premise_nodes.json',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md')

INPUT_SHA256 = {'scripts/admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10.py': '90d9e48440a8a74eabd73553ab61322cf0b75a11de9be1cd65eaee6b5bc6c0db',
 'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_CLOSURE_AUDIT_TWO_BOUNDED_THEOREM_NOTE_2026-08-21.md': '59139166a030e744154115537a01a6b73bf61393e52477459c15b7343a8b1516',
 '.claude/science/physics-loops/toe-axiom-closure-block170-closure-audit-two-20260821/NO_GO_LEDGER.md': '1269fc858695794235b4e0deafc720e98acb22070899186f34254e90af4559fe',
 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
 'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33'}

SOURCE_AST_MAP = {
    "original_block170": {
        "path": "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py",
        "source_sha256": "5d2360f0cb81718a480d77e6eecc303f82cc433299f827148317205c0bf75ea9",
        "nodes": {
            "Bench": [594, 654],
            "observable_families": [688, 733],
            "moment_matrices": [736, 791],
            "structure_flags": [800, 812],
            "cone_probe": [912, 998],
            "moment_probe": [1126, 1298],
            "twist_probe": [1359, 1405],
            "axis_probe": [1408, 1493],
        },
    }
}

BRACKETS = {
    "8x4": (R(12113, 12800), R(807, 800)),
    "12x4": (R(1451, 1280), R(15309, 12800)),
}


class DenseBench:
    def __init__(self, tag: str, cover_t: int, lx: int) -> None:
        self.tag = tag
        self.fixture = h.Fixture(cover_t, lx, tag)
        self.region = h.Bench(self.fixture, SLICE_C)
        self.c = SLICE_C
        self.lx = lx
        self.period = self.fixture.PHYS_T
        self.dimension = self.fixture.PHYS
        self.r = h.dense(
            self.region.reflection, self.dimension, self.dimension
        )
        self.rows = self.region.rows
        self.Hq = h.dense(
            self.fixture.quotient(self.region.hodge), self.dimension, self.dimension
        )
        self.Kq = h.dense(
            self.fixture.quotient_connection(
                self.fixture.edge_d[(0, 0)], self.region.hodge
            ),
            self.dimension,
            self.dimension,
        )
        self.Q = sp.expand(h.MASS * self.Hq + self.Kq)
        self._inverse_cache: dict = {}
        self._moment_cache: dict = {}

    def carrier(self, shear=R(3, 5), sx=R(3, 5), st=R(1, 2), mass=1) -> dict:
        return self.region.carrier(shear=shear, sx=sx, st=st, mass=mass)

    def projection(self, time: int) -> sp.Matrix:
        out = sp.zeros(self.dimension, self.dimension)
        for space in range(self.lx):
            index = self.lx * (time % self.period) + space
            out[index, index] = 1
        return out

    def pair(self, action: sp.MatrixBase, reflection: sp.MatrixBase | None = None,
             rows: tuple[int, ...] | None = None) -> sp.Matrix:
        reflection = self.r if reflection is None else sp.Matrix(reflection)
        rows = self.rows if rows is None else rows
        product = sp.expand(reflection * sp.Matrix(action))
        restricted = product[list(rows), list(rows)]
        return h.herm(restricted)

    def covariance(self, env: dict) -> sp.Matrix:
        key = tuple(sorted((str(symbol), str(value)) for symbol, value in env.items()))
        if key not in self._inverse_cache:
            self._inverse_cache[key] = sp.expand(self.Q.subs(env).inv(method="LU"))
        return self._inverse_cache[key]


def sparse_of(matrix: sp.MatrixBase) -> tuple:
    matrix = sp.Matrix(matrix)
    return tuple(
        (row, column, matrix[row, column])
        for row in range(matrix.rows)
        for column in range(matrix.cols)
        if matrix[row, column] != 0
    )


def observable_families(bench: DenseBench, env: dict, enlarged: bool = False) -> tuple:
    lx, period, dimension = bench.lx, bench.period, bench.dimension
    hodge = sp.expand(bench.Hq.subs(env))

    def unit(time: int, space: int, target_t: int, target_x: int) -> sp.Matrix:
        out = sp.zeros(dimension, dimension)
        out[lx * (time % period) + space % lx,
            lx * (target_t % period) + target_x % lx] = 1
        return out

    def summed(time: int, dt: int, dx: int, weight=lambda _space: 1) -> sp.Matrix:
        return sp.expand(sum(
            (weight(space) * unit(time, space, time + dt, space + dx)
             for space in range(lx)),
            sp.zeros(dimension, dimension),
        ))

    base = (
        ("mass", lambda time: sp.expand(
            bench.projection(time) * hodge * bench.projection(time)
        )),
        ("thop", lambda time: summed(time, 1, 0)),
        ("xhop", lambda time: summed(time, 0, 1)),
        ("plaq", lambda time: summed(time, 1, 1)),
    )
    if not enlarged:
        return base
    return base + (
        ("thop2", lambda time: summed(time, 2, 0)),
        ("aplaq", lambda time: summed(time, 1, -1)),
    )


def gaussian_gram(left, right, covariance: sp.Matrix) -> sp.Matrix:
    sparse_left = [sparse_of(matrix) for matrix in left]
    sparse_right = [sparse_of(matrix) for matrix in right]
    return sp.Matrix(len(left), len(right), lambda i, j: sp.expand(sum(
        (
            sp.conjugate(left_value)
            * right_value
            * covariance[left_row, right_row]
            * covariance[right_column, left_column]
            for left_row, left_column, left_value in sparse_left[i]
            for right_row, right_column, right_value in sparse_right[j]
        ),
        sp.Integer(0),
    )))


def moment_matrices(bench: DenseBench, env: dict, enlarged: bool = False) -> dict:
    key = (
        enlarged,
        tuple(sorted((str(symbol), str(value)) for symbol, value in env.items())),
    )
    if key in bench._moment_cache:
        return bench._moment_cache[key]
    covariance = bench.covariance(env)
    families = observable_families(bench, env, enlarged)
    times = tuple(range(bench.period // 2 + 1))
    operators, labels = [], []
    for name, build in families:
        for offset in times:
            operators.append(sp.expand(build(bench.c + offset)))
            labels.append(f"{name}+{offset}")
    reflected = [sp.expand(bench.r * operator.conjugate() * bench.r)
                 for operator in operators]
    connected = gaussian_gram(operators, operators, covariance)
    reflected_connected = gaussian_gram(reflected, operators, covariance)

    sparse = [sparse_of(operator) for operator in operators]
    one_left = [sp.expand(sum(
        (sp.conjugate(value) * covariance[row, column]
         for row, column, value in entries),
        sp.Integer(0),
    )) for entries in sparse]
    one_right = [sp.expand(sum(
        (value * covariance[column, row] for row, column, value in entries),
        sp.Integer(0),
    )) for entries in sparse]
    full = sp.Matrix(len(operators), len(operators), lambda i, j:
                     sp.expand(connected[i, j] + one_left[i] * one_right[j]))
    result = {
        "labels": tuple(labels),
        "families": tuple(name for name, _ in families),
        "times": times,
        "operators": tuple(operators),
        "connected_raw": connected,
        "full_raw": full,
        "reflected_raw": reflected_connected,
    }
    bench._moment_cache[key] = result
    return result


def family_block(mm: dict, family: str) -> sp.Matrix:
    indices = [index for index, label in enumerate(mm["labels"])
               if label.startswith(family + "+")]
    raw = mm["connected_raw"]
    return raw.extract(indices, indices)


def structure_flags(mm: dict, family: str) -> tuple[bool, bool]:
    block = family_block(mm, family)
    size = block.rows
    hankel = all(
        sp.expand(block[a, b] - block[c, d]) == 0
        for a in range(size) for b in range(size)
        for c in range(size) for d in range(size)
        if a + b == c + d
    )
    toeplitz = all(
        sp.expand(block[a, b] - block[c, d]) == 0
        for a in range(size) for b in range(size)
        for c in range(size) for d in range(size)
        if a - b == c - d
    )
    return hankel, toeplitz


def selected_coefficient_family(bench: DenseBench, env: dict) -> dict:
    hodge = sp.expand(bench.Hq.subs(env))
    generators = [
        sp.expand(bench.projection(bench.c + offset) * hodge
                  * bench.projection(bench.c + offset))
        for offset in range(bench.period // 2 + 1)
    ]
    operators = [operator for generator in generators
                 for operator in (generator, sp.expand(generator * generator))
                 if not h.zero(operator)]
    covariance = bench.covariance(env)
    reflected = [sp.expand(bench.r * operator.conjugate() * bench.r)
                 for operator in operators]
    raw = gaussian_gram(operators, operators, covariance)
    reflected_raw = gaussian_gram(reflected, operators, covariance)
    return {
        "kind": "selected coefficient powers {G_t,G_t^2}",
        "dimension": len(operators),
        "raw_hermitian": h.zero(raw - raw.H),
        "hermitian_part_inertia": h.inertia_pzn(h.herm(raw)),
        "reflected_hermitian_part_inertia": h.inertia_pzn(h.herm(reflected_raw)),
    }


def moment_table(bench: DenseBench) -> dict:
    lo, hi = BRACKETS[bench.tag]
    endpoints = {}
    for mass in (lo, hi):
        mm = moment_matrices(bench, bench.carrier(mass=mass))
        endpoints[mass] = {
            "connected_raw_hermitian": h.zero(mm["connected_raw"] - mm["connected_raw"].H),
            "full_raw_hermitian": h.zero(mm["full_raw"] - mm["full_raw"].H),
            "connected_hermitian_part": h.inertia_pzn(h.herm(mm["connected_raw"])),
            "full_hermitian_part": h.inertia_pzn(h.herm(mm["full_raw"])),
            "reflected_hermitian_part": h.inertia_pzn(h.herm(mm["reflected_raw"])),
        }
    low_mm = moment_matrices(bench, bench.carrier(mass=lo))
    enlarged = moment_matrices(bench, bench.carrier(mass=lo), enlarged=True)
    small_n = low_mm["full_raw"].rows
    principal = h.zero(
        enlarged["full_raw"][:small_n, :small_n] - low_mm["full_raw"]
    )
    benchmark = moment_matrices(bench, bench.carrier(mass=1))
    structures = {
        family: structure_flags(benchmark, family)
        for family in benchmark["families"]
    }
    selected = {
        mass: selected_coefficient_family(bench, bench.carrier(mass=mass))
        for mass in (sp.Integer(1), R(1, 10))
    }
    return {
        "endpoints": endpoints,
        "principal_extension": principal,
        "small_dimension": small_n,
        "large_dimension": enlarged["full_raw"].rows,
        "selected_structure": structures,
        "selected_coefficients": selected,
    }


def twist_battery(bench: DenseBench) -> tuple:
    lx, period, dimension = bench.lx, bench.period, bench.dimension

    def diagonal_sign(build) -> sp.Matrix:
        return sp.diag(*[
            sp.Integer(build(index // lx, index % lx))
            for index in range(dimension)
        ])

    def shift_x() -> sp.Matrix:
        out = sp.zeros(dimension, dimension)
        for time in range(period):
            for space in range(lx):
                out[lx * time + space, lx * time + (space + 1) % lx] = 1
        return out

    def shift_t() -> sp.Matrix:
        out = sp.zeros(dimension, dimension)
        for time in range(period):
            for space in range(lx):
                out[lx * time + space, lx * ((time + 1) % period) + space] = (
                    -1 if time + 1 == period else 1
                )
        return out

    parity = diagonal_sign(lambda time, space: (-1) ** (time + space))
    sx, st = shift_x(), shift_t()
    return (
        ("eps", parity),
        ("eps_t", diagonal_sign(lambda time, _space: (-1) ** time)),
        ("eps_x", diagonal_sign(lambda _time, space: (-1) ** space)),
        ("shift_x", sx),
        ("taste_x", sp.expand(parity * sx)),
        ("shift_t", st),
        ("taste_t", sp.expand(parity * st)),
        ("phase_i", I * sp.eye(dimension)),
    )


def twist_table(bench: DenseBench) -> dict:
    env = bench.carrier()
    action = sp.expand(bench.Q.subs(env))
    benchmark_components = h.fixed_support_components(action)
    zero_components = h.fixed_support_components(
        sp.expand(bench.Q.subs(bench.carrier(st=0)))
    )
    cells = []
    for name, unitary in twist_battery(bench):
        reflection = sp.expand(unitary * bench.r)
        cells.append((
            name,
            h.zero(reflection * reflection - sp.eye(bench.dimension)),
            h.zero(sp.expand(unitary.H * action * unitary) - action),
            h.inertia_pzn(bench.pair(bench.Q, reflection).subs(env)),
        ))
    plus = bench.pair(bench.Q, bench.r).subs(env)
    minus = bench.pair(bench.Q, -bench.r).subs(env)
    global_phases = {"sign_identity": h.zero(plus + minus)}
    for name, unitary in (("+I", sp.eye(bench.dimension)),
                          ("-I", -sp.eye(bench.dimension))):
        reflection = sp.expand(unitary * bench.r)
        global_phases[name] = (
            h.zero(reflection * reflection - sp.eye(bench.dimension)),
            h.zero(sp.expand(unitary.H * action * unitary) - action),
            h.inertia_pzn(bench.pair(bench.Q, reflection).subs(env)),
        )
    return {
        "benchmark_components": benchmark_components,
        "st_zero_components": zero_components,
        "finite_battery": tuple(cells),
        "global_phases": global_phases,
    }


def axis_table(bench: DenseBench) -> dict:
    fixture = bench.fixture
    flat = fixture.flat_moduli()
    hodge = fixture.cover_hodge(*flat)
    flat_action = h.dense(
        fixture.quotient_action(fixture.edge_d[(0, 0)], hodge, h.MASS),
        fixture.PHYS,
        fixture.PHYS,
    )
    action_a = sp.expand(flat_action.subs({h.MASS: 1, h.SX: R(3, 5), h.ST: R(1, 2)}))
    action_b = sp.expand(flat_action.subs({h.MASS: 1, h.SX: R(1, 2), h.ST: R(3, 5)}))
    reports = []
    if fixture.PHYS_T == fixture.LX:
        exchange = sp.zeros(fixture.PHYS, fixture.PHYS)
        for time in range(fixture.PHYS_T):
            for space in range(fixture.LX):
                exchange[fixture.LX * time + space, fixture.LX * space + time] = 1
        for name, candidate in (
            ("A", action_a),
            ("A^T", action_a.T),
            ("conj(A)", action_a.conjugate()),
            ("A^H", action_a.H),
        ):
            mapped = sp.expand(exchange.T * candidate * exchange)
            reports.append((name, h.zero(mapped - action_b)))

    spatial_reflection = sp.zeros(fixture.PHYS, fixture.PHYS)
    for time in range(fixture.PHYS_T):
        for space in range(fixture.LX):
            spatial_reflection[
                fixture.LX * time + space,
                fixture.LX * time + ((1 - space) % fixture.LX),
            ] = 1
    columns = tuple(
        fixture.LX * time + space
        for time in range(fixture.PHYS_T)
        for space in (0, 1)
    )
    spatial = {
        st: h.inertia_pzn(
            bench.pair(bench.Q, spatial_reflection, columns).subs(bench.carrier(st=st))
        )
        for st in (0, R(1, 8), R(1, 2), 2, -R(1, 2))
    }
    return {"four_maps": tuple(reports), "spatial_five_points": spatial}


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    checks.add("A-input-identity", identity_ok, f"nine exact inputs; actual={actual}")

    benches = {
        tag: DenseBench(tag, cover_t, lx)
        for tag, cover_t, lx in (("8x4", 8, 4), ("12x4", 12, 4))
    }
    recipe = {
        tag: (
            h.zero(bench.Kq + bench.Kq.H),
            h.zero(h.herm(bench.Q) - h.MASS * bench.Hq),
        )
        for tag, bench in benches.items()
    }
    checks.add(
        "B-recipe-level-antihermiticity",
        all(row == (True, True) for row in recipe.values()),
        f"the identity is a property of i(Hd+d^H H) and does not decide reflected positivity; {recipe}",
    )

    moments = {tag: moment_table(bench) for tag, bench in benches.items()}
    endpoint_ok = all(
        row["endpoints"][BRACKETS[tag][0]]["full_hermitian_part"][2] > 0
        and row["endpoints"][BRACKETS[tag][1]]["full_hermitian_part"][2] == 0
        for tag, row in moments.items()
    )
    checks.add(
        "C-endpoint-signs-only",
        endpoint_ok and HISTORICAL_BISECTION_STEPS == 7,
        f"the historical seven-step process supplies these two endpoint signs per fixture, without monotonicity or a unique critical mass; {moments}",
    )
    checks.add(
        "D-raw-versus-hermitian-part",
        all(
            all("connected_raw_hermitian" in cell and "connected_hermitian_part" in cell
                for cell in row["endpoints"].values())
            for row in moments.values()
        ),
        "raw moment matrices are reported separately; PSD of a Hermitian part is not promoted to raw-functional positivity",
    )
    checks.add(
        "E-selected-coefficient-family",
        all(
            all(cell["kind"] == "selected coefficient powers {G_t,G_t^2}"
                for cell in row["selected_coefficients"].values())
            for row in moments.values()
        ),
        "the finite family is not called the full bilinear-generated star algebra; mixed observable products would be quartic",
    )
    checks.add(
        "F-principal-submatrix-and-structure-scope",
        all(
            row["principal_extension"]
            and row["large_dimension"] > row["small_dimension"]
            for row in moments.values()
        ),
        "the named small matrix is a leading principal submatrix of one named extension; negative directions persist, while Hankel/Toeplitz flags concern only the selected families",
    )

    twists = {tag: twist_table(bench) for tag, bench in benches.items()}
    checks.add(
        "G-fixed-benchmark-twists",
        all(
            row["benchmark_components"] == 1
            and row["global_phases"]["+I"][:2] == (True, True)
            and row["global_phases"]["-I"][:2] == (True, True)
            and row["global_phases"]["sign_identity"]
            for row in twists.values()
        ),
        f"connected support is fixed-benchmark evidence; both global +/-I are legitimate and -r negates the pairing; {twists}",
    )

    axes = {tag: axis_table(bench) for tag, bench in benches.items()}
    checks.add(
        "H-finite-axis-table",
        len(axes["8x4"]["four_maps"]) == 4
        and all(not success for _, success in axes["8x4"]["four_maps"])
        and all(len(row["spatial_five_points"]) == 5 for row in axes.values()),
        f"four failed exchange maps and five spatial samples are retained as finite results, not an independence proof; {axes}",
    )
    checks.add(
        "I-exact-bounded-scope",
        h.no_float((recipe, moments, twists, axes)) and len(SOURCE_AST_MAP) == 1,
        "two primary fixtures and named families only; no all-variant, transfer-exhaustion, or physical closure",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
