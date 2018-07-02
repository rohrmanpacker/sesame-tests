import sesame
import numpy as np

length = 6e-4  # length of the system in cm

mesh = np.linspace(0, 6e-4)

sys = sesame.Builder(mesh)

material = {'Nc': 1e+19, 'Nv':1e+19, 'Eg':1.1, 'affinity':0, 'epsilon':10,
        'mu_e':300, 'mu_h':300, 'tau_e':1e-9, 'tau_h':1e-9, 'Et':0}

