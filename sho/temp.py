import numpy as np


def proportional(i: int, max_iter: int):
    return max_iter/(i+1)


def square(i: int, max_iter: int):
    return max_iter/(i*i)


def logarithmic(i: int, max_iter: int):
    return max_iter/np.log(i)
