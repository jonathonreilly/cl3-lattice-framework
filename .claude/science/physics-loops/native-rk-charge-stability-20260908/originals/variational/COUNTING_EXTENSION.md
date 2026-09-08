# Exact degree counting improves the variational constant

This supplements, without modifying, the frozen ordered-hole proof. Root and author independently identified the same counting refinement before these new controls. The ordered-hole phase theorem remains a prerequisite.

Partition all finite D2 edge configurations into B (adjacent charges whose common edge has an eligible bit) and C (all others). The exact permitted-hop degree is6 on B and8 on C: each charge has4 eligible edges, and only an eligible shared edge is lost, once from each charge. Thus mean degree=8-2|B|/(|B|+|C|).

Flipping the shared eligible edge in a B configuration yields an ice configuration. Conversely flipping any edge of any ice configuration yields a unique B configuration. The inverse recovers both the ice configuration and the common edge. Consequently |B|=|E|N_ice exactly, retaining all geometrical edge multiplicities and all winding sectors.

For the bound, count allowed hopping edges between B and C. Every B configuration has exactly6 such edges: any allowed move separates its adjacent charges into distinct same-sublattice positions, which cannot be adjacent. Conversely a C configuration can have at most4 B neighbors. A single hop can make the two charge positions adjacent only by moving one charge to a common neighbor of the original two positions. Any distinct vertices in the specified cubic torus have at most2 common neighbors: coordinate displacements allowing a two-step path are two unit steps along one axis (at most2 intermediate choices, including extent4 wraparound) or one step along each of two axes (2 choices). There are two choices of which signed charge moves. Bit/low-charge eligibility can only reduce these4 possibilities. Hopping reversibility therefore gives

 6|B| <= 4|C|,
 average degree >= 8-2/(1+3/2)=36/5.

The phase-correct trial from the original proof yields

 E_D2 <= 2U-(36/5)|t|.

Together with the existing lower bound,2U-8|t|<=E_D2<=2U-(36/5)|t|. In particular U<(18/5)|t| makes this trial negative, so neutral zero states are not global ground states. The gap between this necessary neutral-stability condition and the sufficient U>=4|t| remains unresolved.

The exact expression8-2|E|N_ice/N_D2 suggests a route toward8 if the ratio can be bounded to zero with volume, but no such counting estimate is proved here. Static all-position support alone does not control relative numbers of configurations. No operator eigenvector or exact charged eigenvalue is inferred from the trial. The entire construction remains restricted to one positive and one negative charge; its removal of hopping signs does not extend automatically to same-species exchanges.
