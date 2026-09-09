"""Selected finite menu definitions from the exact #7326 input bodies.

No spatial compiler, source-selection theorem, or historical controller is imported.
See the canonical Gaussian note for the conditional mathematical domain.
"""


from __future__ import annotations


from dataclasses import dataclass


from sympy import I, Matrix, Rational as Q, simplify, sqrt


I2 = Matrix.eye(2)


SX = Matrix([[0, 1], [1, 0]])


SZ = Matrix([[1, 0], [0, -1]])


def matrix_equal(left: Matrix, right: Matrix) -> bool:
    return left.shape == right.shape and all(
        simplify(left[row, column] - right[row, column]) == 0
        for row in range(left.rows)
        for column in range(left.cols)
    )


def hermitian_part(value: Matrix) -> Matrix:
    return simplify((value + value.conjugate().T) / 2)


def antihermitian_coefficient(value: Matrix) -> Matrix:
    return simplify((value - value.conjugate().T) / (2 * I))


SECTOR_MASSES = {
    "RRR": Q(1, 4),
    "RR": Q(1, 8),
    "RRI": Q(1, 4),
    "III": Q(1, 4),
    "II": Q(1, 8),
}


COEFFICIENT_DENSITIES = {
    "RRR": Q(2),  # normalized area density on the area-1/2 triangle
    "RR": Q(1),   # unit point mass on the coefficient-free stratum
    "RRI": Q(1),  # normalized length density on [0,1]
    "III": Q(2),  # normalized area density on the area-1/2 simplex
    "II": Q(1),   # normalized length density on [0,1]
}


SECTOR_TAGS = {"RRR": Q(0), "RR": Q(1), "RRI": Q(2), "III": Q(4), "II": Q(5)}


OUTCOME_LABELS = (Q(30), Q(31), Q(32))


@dataclass(frozen=True)
class MenuPayload:
    sector: str
    parameters: tuple
    preparation: Matrix
    x_axis: Matrix
    z_axis: Matrix


@dataclass(frozen=True)
class OutcomeSpec:
    name: str
    effect: Matrix
    label: Q

    @property
    def content(self) -> Matrix:
        return simplify(self.effect + I * self.label * I2)


def truth_nonnegative(value) -> bool:
    return bool(simplify(value).is_nonnegative)


def truth_positive(value) -> bool:
    return bool(simplify(value).is_positive)


def scalar_part(value: Matrix):
    return simplify(value.trace() / 2)


def traceless_part(value: Matrix) -> Matrix:
    return simplify(value - scalar_part(value) * I2)


def pauli_radius(value: Matrix):
    return simplify(sqrt((value * value).trace() / 2))


def is_axis(value: Matrix) -> bool:
    return (
        matrix_equal(value, value.conjugate().T)
        and simplify(value.trace()) == 0
        and matrix_equal(simplify(value * value), I2)
    )


def payload_rrr(a, b, x_axis: Matrix = SX, z_axis: Matrix = SZ) -> Matrix:
    return simplify((1 + a) * x_axis + I * (1 + b) * z_axis)


def payload_rr(x_axis: Matrix = SX, z_axis: Matrix = SZ) -> Matrix:
    return simplify(x_axis + I * (z_axis + SECTOR_TAGS["RR"] * I2))


def payload_rri(d, x_axis: Matrix = SX, z_axis: Matrix = SZ) -> Matrix:
    return simplify((1 + d) * x_axis + I * (z_axis + SECTOR_TAGS["RRI"] * I2))


def payload_iii(d1, d2, x_axis: Matrix = SX, z_axis: Matrix = SZ) -> Matrix:
    return simplify(
        (1 + d1) * x_axis
        + I * ((1 + d2) * z_axis + SECTOR_TAGS["III"] * I2)
    )


def payload_ii(d, x_axis: Matrix = SX, z_axis: Matrix = SZ) -> Matrix:
    return simplify((1 + d) * x_axis + I * (z_axis + SECTOR_TAGS["II"] * I2))


def decode_menu_payload(value: Matrix) -> MenuPayload | None:
    h_value = hermitian_part(value)
    k_value = antihermitian_coefficient(value)
    if simplify(h_value.trace()) != 0:
        return None
    h_zero = traceless_part(h_value)
    k_zero = traceless_part(k_value)
    h_radius = pauli_radius(h_zero)
    k_radius = pauli_radius(k_zero)
    if not truth_positive(h_radius) or not truth_positive(k_radius):
        return None
    x_axis = simplify(h_zero / h_radius)
    z_axis = simplify(k_zero / k_radius)
    if not (
        is_axis(x_axis)
        and is_axis(z_axis)
        and matrix_equal(simplify(x_axis * z_axis + z_axis * x_axis), Matrix.zeros(2))
    ):
        return None
    tag = scalar_part(k_value)
    sector = next(
        (name for name, candidate in SECTOR_TAGS.items() if simplify(tag - candidate) == 0),
        None,
    )
    if sector is None:
        return None
    if sector == "RRR":
        a, b = simplify(h_radius - 1), simplify(k_radius - 1)
        valid = (
            truth_nonnegative(a)
            and truth_nonnegative(1 - a)
            and truth_nonnegative(b)
            and truth_nonnegative(1 - b)
            and truth_nonnegative(a + b - 1)
        )
        parameters = (a, b)
    elif sector == "RR":
        valid = simplify(h_radius - 1) == 0 and simplify(k_radius - 1) == 0
        parameters = tuple()
    elif sector == "RRI":
        d = simplify(h_radius - 1)
        valid = (
            simplify(k_radius - 1) == 0
            and truth_nonnegative(d)
            and truth_nonnegative(1 - d)
        )
        parameters = (d,)
    elif sector == "III":
        d1, d2 = simplify(h_radius - 1), simplify(k_radius - 1)
        valid = (
            truth_nonnegative(d1)
            and truth_nonnegative(d2)
            and truth_nonnegative(1 - d1 - d2)
        )
        parameters = (d1, d2)
    else:
        d = simplify(h_radius - 1)
        valid = (
            simplify(k_radius - 1) == 0
            and truth_nonnegative(d)
            and truth_nonnegative(1 - d)
        )
        parameters = (d,)
    if not valid:
        return None
    return MenuPayload(sector, parameters, I2 / 2, x_axis, z_axis)


def projector(axis: Matrix) -> Matrix:
    return simplify((I2 + axis) / 2)


def nonzero_rows(rows):
    return tuple(
        (index, name, simplify(effect))
        for index, (name, effect) in enumerate(rows)
        if not matrix_equal(effect, Matrix.zeros(2))
    )


def menu_specs(value: Matrix) -> tuple[OutcomeSpec, ...] | None:
    decoded = decode_menu_payload(value)
    if decoded is None:
        return None
    x_axis, z_axis = decoded.x_axis, decoded.z_axis
    if decoded.sector == "RRR":
        a, b = decoded.parameters
        c = simplify(2 - a - b)
        if simplify(a) == 0:
            rows = (("rrr-1", Matrix.zeros(2)), ("rrr-2", projector(z_axis)), ("rrr-3", projector(-z_axis)))
        elif simplify(b) == 0:
            rows = (("rrr-1", projector(x_axis)), ("rrr-2", Matrix.zeros(2)), ("rrr-3", projector(-x_axis)))
        elif simplify(c) == 0:
            rows = (("rrr-1", projector(x_axis)), ("rrr-2", projector(-x_axis)), ("rrr-3", Matrix.zeros(2)))
        else:
            gamma = simplify((c * c - a * a - b * b) / (2 * a * b))
            eta = simplify(sqrt(1 - gamma * gamma))
            n1 = x_axis
            n2 = simplify(gamma * x_axis + eta * z_axis)
            n3 = simplify(-(a * n1 + b * n2) / c)
            rows = (
                ("rrr-1", simplify(a * projector(n1))),
                ("rrr-2", simplify(b * projector(n2))),
                ("rrr-3", simplify(c * projector(n3))),
            )
    elif decoded.sector == "RR":
        rows = (("rr-1", projector(x_axis)), ("rr-2", projector(-x_axis)))
    elif decoded.sector == "RRI":
        (d,) = decoded.parameters
        rows = (
            ("rri-i", simplify(d * I2)),
            ("rri-plus", simplify((1 - d) * projector(x_axis))),
            ("rri-minus", simplify((1 - d) * projector(-x_axis))),
        )
    elif decoded.sector == "III":
        d1, d2 = decoded.parameters
        rows = (
            ("iii-1", simplify(d1 * I2)),
            ("iii-2", simplify(d2 * I2)),
            ("iii-3", simplify((1 - d1 - d2) * I2)),
        )
    else:
        (d,) = decoded.parameters
        rows = (("ii-1", simplify(d * I2)), ("ii-2", simplify((1 - d) * I2)))
    present = nonzero_rows(rows)
    return tuple(
        OutcomeSpec(name, effect, OUTCOME_LABELS[index])
        for index, name, effect in present
    )


def terminal_law(value: Matrix, variant: str = "trace"):
    specs = menu_specs(value)
    decoded = decode_menu_payload(value)
    if specs is None or decoded is None:
        return None
    masses = [simplify((decoded.preparation * spec.effect).trace()) for spec in specs]
    if variant == "context-skew" and decoded.sector == "RRR" and len(specs) == 3:
        scales = [simplify(spec.effect.trace()) for spec in specs]
        delta = simplify(scales[0] * scales[1] * scales[2] / 10)
        masses[0] = simplify(masses[0] + delta / 2)
        masses[1] = simplify(masses[1] + delta / 2)
        masses[2] = simplify(masses[2] - delta)
    elif variant not in ("trace", "context-skew"):
        raise ValueError(f"unknown terminal-law variant: {variant}")
    return tuple((spec.content, mass) for spec, mass in zip(specs, masses))
