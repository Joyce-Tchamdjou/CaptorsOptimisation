########################################################################
# Algorithms
########################################################################
import numpy as np
from numpy.ma.core import shape, var
from numpy.random.mtrand import uniform

def random(func, init, again):
    """Iterative random search template."""
    best_sol = init()
    best_val = func(best_sol)
    val,sol = best_val,best_sol
    i = 0
    while again(i, best_val, best_sol):
        sol = init()
        val = func(sol)
        if val >= best_val:
            best_val = val
            best_sol = sol
        i += 1
    return best_val, best_sol


def greedy(func, init, neighb, again):
    """Iterative randomized greedy heuristic template."""
    best_sol = init()
    best_val = func(best_sol)
    val,sol = best_val,best_sol
    i = 1
    while again(i, best_val, best_sol):
        sol = neighb(best_sol)
        val = func(sol)
        # Use >= and not >, so as to avoid random walk on plateus.
        if val >= best_val:
            best_val = val
            best_sol = sol
        i += 1
    return best_val, best_sol

# TODO add a simulated-annealing template.
def simulated_annealing(func, init, neighb, again, proba, temp):
    """Simulated annealing heuristic template."""
    print("Starting Simulated Annealing")
    best_sol = init()
    best_val = func(best_sol)
    val, sol = best_val, best_sol
    i = 0
    while again(i, best_val, best_sol):
        sol = neighb(best_sol)
        val = func(sol)
        # Use >= and not >, so as to avoid random walk on plateus.
        if val >= best_val or np.random.rand() < proba(val, best_val, temp(i)):
            best_val = val
            best_sol = sol
        i += 1
    return best_val, best_sol
    

# TODO add a population-based stochastic heuristic template.
def population_based(func, init, again, variation, n):
    print("Starting population based algorithm")
    best_sol = [init() for i in range(n)]
    best_val = [func(best_sol[i]) for i in range(n)]
    i = 0
    while again(i, best_val[0], best_sol[0]):
        population_sol = best_sol
        offsprings = variation(best_sol)
        population_sol.extend(offsprings)
        population_val = [func(population_sol[j]) for j in range(len(population_sol))]
        best = np.argsort(population_val)[::-1][0:n]
        best_sol = [population_sol[best[j]] for j in range(n)]
        best_val = [population_val[best[j]] for j in range(n)]
        i += 1
    return best_val[0], best_sol[0]












