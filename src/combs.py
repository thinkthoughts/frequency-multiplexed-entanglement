import numpy as np

def frequency_comb(center=0, spacing=1, n_modes=10):
    n = np.arange(-n_modes, n_modes + 1)
    return center + spacing * n
