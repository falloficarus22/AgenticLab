class SymbolicSolver:
    name = 'symbolic_solver'

    def can_handle(self, plan):
        return 'symbolic' in str(plan).lower

    def run(self, plan):
        return {"solution": "symbolic result"}
        