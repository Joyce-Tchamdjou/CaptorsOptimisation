import numpy as np

def variate(parents):
    P = []
    m = np.mean(parents)
    v = np.var(parents)
    for x in parents:
        P.append( x + ((np.random.normal(m, v) - m)/v) )
    return P