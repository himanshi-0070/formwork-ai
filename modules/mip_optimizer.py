from ortools.linear_solver import pywraplp

def optimize_moulds(total_quantity, reuse_limit):

    solver = pywraplp.Solver.CreateSolver('SCIP')

    x = solver.IntVar(0, total_quantity, 'moulds')

    solver.Add(x * reuse_limit >= total_quantity)

    solver.Minimize(x)

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        return int(x.solution_value())
    else:
        return None
