# Post-execution mutation amendment

The preregistered mutations 1 and 2 were mathematically too weak. Removing
only one member of the `X` or `Y` projector pair leaves five projectors of
rank 4, so rejection by an exact-six cardinality check would not test the
span theorem. They are replaced by:

1. `drop_x_axis_pair`: remove both `P_{X,+}` and `P_{X,-}`; the coordinate
   rank must fall from 4 to 3;
2. `drop_y_axis_pair`: remove both `P_{Y,+}` and `P_{Y,-}`; the coordinate
   rank must fall from 4 to 3.

Nine post-prereg attack mutations cover surfaces added or sharpened during
execution:

| mutation | designated failure |
|---|---|
| `nonorthogonal_record_pointer` | Record pointer projectors cease to be orthogonal/exhaustive |
| `non_even_global_pointer` | an `X` pointer fails the global `Z_R` parity check |
| `break_induced_cubic_action` | one projective representative no longer realizes its declared cubic conjugation |
| `linearize_projective_lifts` | falsely requiring exact unitary multiplication rejects the genuine spin lift |
| `drop_record_generator` | the derived Record-algebra rank and generated dimension fall |
| `matter_record_overlap` | a claimed Record generator acts on matter and fails separation/commutation |
| `privilege_lattice_direction` | the common Admissibility kernel fails cubic covariance |
| `record_not_permanent` | the second local use flips the formed Record |
| `constant_admissibility_rule` | the distribution no longer varies with neighboring conditions |

The final hostile suite therefore contains 31 mutations. This amendment
changes no target theorem; it corrects the executable refutation coverage.
