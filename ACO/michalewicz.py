import numpy as np

def MICHALEWICZ(x):
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange(1., n+1)
    return - sum(np.sin(x) * np.sin(j * x**2 / np.pi ) ** (2 * 10))

OPSEG_MICHALEWICZ = [0, np.pi]
