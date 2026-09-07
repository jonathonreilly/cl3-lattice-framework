# Postexecution mutation audit

Baseline execution returns `TOTAL: PASS=16 FAIL=0`.

All 27 preregistered mutations are killed. Eleven postexecution mutations were
added in response to independent review:

1. `treat_blank_as_independent_binary_marginal`
2. `skip_record_actualization_instrument`
3. `leave_record_incident_hopping_on`
4. `external_cube_bonds_left_on`
5. `break_rotated_cube_gauge_covariance`
6. `wrong_edge_exponential_weight`
7. `treat_source_preparation_as_permanent_record`
8. `claim_star_gibbs_is_record_update_dynamics`
9. `break_signed_cube_adjacency_lift`
10. `treat_coordinate_paulis_as_physical_site_qubits`
11. `branch_specific_cube_protocol`

Final result: `38` killed, `0` survived. The added mutations guard the exact
places where the preregistered wording was too broad: blank semantics,
action-versus-kernel supply, Record actualization/permanence, cube boundary
isolation, physical CAR typing, rotational gauge covariance, and a genuinely
common protocol.
