# Three-site constructive supplement, frozen before execution

Same nine-qubit reduced carrier, K, source and target; expanded workspace (no P_legal constraint), complete graph only. Permit Hermitian controls of Pauli weight at most3. The local pulse law, durations and coherent typing remain supplied, not an interaction primitive or NN synthesis. No new ancillas or energy changes.

Freeze n_j=(I-Z_j)/2, q=n_f, Pi=(I+Y_x)/2. Let T=|0><1|_f tensor |1><0|_b1 and H1=Pi(T+T†). Pulse U1=exp(-i pi H1/2). It exchanges charged fuel with the high battery bit only in Y+. Then H2=(I-q)X_x, U2=exp(-i pi H2/4). Then H3=|01><10|_head+h.c., U3=exp(-i pi H3/2). Finally H4=X_l1, U4=exp(-i pi H4/2), where label string is explicitly l0 l1=01 for accepted plus. Source/target battery notation remains b1 b0.

Predicted states: U1 produces -i times (Y+,f0,battery10); U2 maps Y+ exactly to Z+; U3 moves head10 to01 with another -i; U4 sets label01 with another -i. Final state is i times target. The durations/signs are fixed before execution.

Check exact full Pauli-sum commutators with K,Z_r,N_head, maximum supports, and exact sparse state after EACH pulse. Exponentiate analytically using H^3=H for H1/H3, H2²=1-q, and H4²=I. Check their stated polynomial identities and unitary identities, not only endpoint amplitudes. Verify H1 is genuinely weight3 and deleting its Y control fails [H,K]. This is an exact state-transfer construction, not implementation of complete K instrument, cap/refusal channel or permanent fresh Record formation. Old Record remains fixed; new label is workspace until supplied decoupling/readout.

The existing exact commutant runner will be frozen as a standalone scratch artifact with explicit fixture/support metadata, canonical basis hashes and resource checks. This is metadata packaging of the already frozen two-site calculation, not a revised numerical test.
