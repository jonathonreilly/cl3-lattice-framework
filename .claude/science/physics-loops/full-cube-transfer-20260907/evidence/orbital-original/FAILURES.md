# Preserved first execution failure

The first run stopped at SymPy ordering a radical eigenvalue of the positive rational cycle metric. No scientific check failed: SymPy could not determine the truth value of a complex-radical expression >0. Original source is check_before_symbolic_order_fix.py. The fix uses exact positive leading principal minors (Sylvester criterion), with no graph, parameter or expected spectrum change. Empty initial stdout did not constitute a result.
