from producer_original import *

@njit(cache=True)
def prepare_with_samples(
    start_state: np.ndarray,
    delta_v: float,
    population: int,
    classical_sweeps: int,
    burn_sweeps: int,
    plaquette_links: np.ndarray,
    affected_plaquettes: np.ndarray,
    affected_counts: np.ndarray,
    resample_interval: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray, float, float]:
    np.random.seed(seed)
    states = np.empty((population, start_state.shape[0]), dtype=np.uint8)
    counts = np.empty(population, dtype=np.int32)
    for walker in range(population):
        states[walker] = start_state
        counts[walker] = count_flippable(states[walker], plaquette_links)
    ancestors = np.arange(population, dtype=np.int32)
    labels = np.full((1, population), -1, dtype=np.int32)
    for _ in range(classical_sweeps):
        for step in range(plaquette_links.shape[0]):
            for walker in range(population):
                plaquette = np.random.randint(plaquette_links.shape[0])
                if is_flippable(states[walker], plaquette_links[plaquette]):
                    counts[walker] = flip_and_update_count(
                        states[walker],
                        plaquette,
                        counts[walker],
                        plaquette_links,
                        affected_plaquettes,
                        affected_counts,
                    )
    sample_count = min(40, burn_sweeps)
    count_samples = np.empty(sample_count, dtype=np.float64)
    minimum_effective_population = float(population)
    for sweep in range(burn_sweeps):
        states, counts, ancestors, labels, effective_population = propagate_sweep(
            states,
            counts,
            ancestors,
            labels,
            delta_v,
            plaquette_links,
            affected_plaquettes,
            affected_counts,
            resample_interval,
        )
        minimum_effective_population = min(
            minimum_effective_population, effective_population
        )
        if sweep >= burn_sweeps - sample_count:
            count_samples[sweep - burn_sweeps + sample_count] = np.mean(counts)
    return (
        states,
        counts,
        float(np.mean(count_samples)),
        minimum_effective_population,
        count_samples.copy(),
    )
