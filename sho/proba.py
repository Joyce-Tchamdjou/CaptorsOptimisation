import numpy as np


def exponential(val: float, best_val: float, temperature: float):
    return np.exp((val - best_val)/temperature)
