import numpy as np
from producer_original import evaluate_observables, propagate_sweep

def measure_raw_block(
    states: np.ndarray,
    counts: np.ndarray,
    delta_v: float,
    tau_max: int,
    forward_sweeps: int,
    coefficient_real: np.ndarray,
    coefficient_imag: np.ndarray,
    plaquette_links: np.ndarray,
    affected_plaquettes: np.ndarray,
    affected_counts: np.ndarray,
    interval: int,
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    float,
    float,
    np.ndarray,
    np.ndarray,
]:
    population = states.shape[0]
    mode_count = coefficient_real.shape[0]
    origin_observables = evaluate_observables(
        states, coefficient_real, coefficient_imag
    )
    tau_count = tau_max + 1
    ancestors = np.arange(population, dtype=np.int32)
    labels = np.full((tau_count, population), -1, dtype=np.int32)
    tau_origins = np.full((tau_count, population), -1, dtype=np.int32)
    tau_observables = np.zeros(
        (tau_count, population, mode_count), dtype=np.complex128
    )
    labels[0] = np.arange(population, dtype=np.int32)
    tau_origins[0] = ancestors
    tau_observables[0] = origin_observables
    minimum_effective = float(population)
    correlation = np.zeros((tau_count, mode_count), dtype=np.complex128)
    survival = np.zeros(tau_count, dtype=float)
    origin_diversity = np.zeros(tau_count, dtype=float)
    origin_diversity[0] = 1.0
    for sweep in range(tau_max + forward_sweeps + 1):
        if sweep > 0 and sweep <= tau_max:
            labels[sweep] = np.arange(population, dtype=np.int32)
            tau_origins[sweep] = ancestors
            tau_observables[sweep] = evaluate_observables(
                states, coefficient_real, coefficient_imag
            )
            origin_diversity[sweep] = len(np.unique(ancestors)) / population
        if sweep >= forward_sweeps:
            tau = sweep - forward_sweeps
            if tau <= tau_max:
                final_labels = labels[tau]
                survival[tau] = len(np.unique(final_labels)) / population
                products = np.empty(
                    (population, mode_count), dtype=np.complex128
                )
                for walker, label in enumerate(final_labels):
                    origin = tau_origins[tau, label]
                    products[walker] = origin_observables[origin] * np.conjugate(
                        tau_observables[tau, label]
                    )
                correlation[tau] = np.mean(products, axis=0)
        if sweep == tau_max + forward_sweeps:
            break
        states, counts, ancestors, labels, effective = propagate_sweep(
            states,
            counts,
            ancestors,
            labels,
            delta_v,
            plaquette_links,
            affected_plaquettes,
            affected_counts,
            interval,
        )
        minimum_effective = min(minimum_effective, effective)
    return (
        states,
        counts,
        correlation,
        minimum_effective,
        len(np.unique(ancestors)) / population,
        origin_diversity,
        survival,
    )
