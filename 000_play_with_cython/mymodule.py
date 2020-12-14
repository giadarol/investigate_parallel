import numpy as np

def testfun(x, n):
    y = 1.
    for ii in range(n):
        y += ii*np.sqrt(x)
    return y
