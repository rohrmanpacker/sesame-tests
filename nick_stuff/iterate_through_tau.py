import sesame
from sesame.ui import sim
from sesame import analyzer,utils,builder
import numpy as np
import matplotlib.pyplot as plt
import random

length = 6e-4  # length of the system in cm

mesh = np.linspace(0, length)
nD = 1e+16
nA = 1e+16

tau_to_test = [1e-9,1e-8,1e-7,1e-6,1e-5]

center = np.linspace(2e-4,5e-4,20)
x0 = center[random.randint(0,20)]
f = lambda x: 1e+19 * np.exp((-(x-x0)**2)/(2e-6**2))
plt.figure()
for i in range(len(tau_to_test)):
    sys = builder.Builder(mesh)

    # Add the doping
    sys.add_donor(nD, lambda x: x < 3e-4)
    sys.add_acceptor(nA, lambda x: x > 3e-4)
    # Define Ohmic contacts
    sys.contact_type('Ohmic', 'Ohmic')
    # Define the surface recombination velocities for electrons and holes [cm/s]
    Sn_left, Sp_left, Sn_right, Sp_right = 1e5, 0, 0, 1e5
    sys.contact_S(Sn_left, Sp_left, Sn_right, Sp_right)
    # create the material
    material = {'Nc': 1e+19, 'Nv': 1e+19, 'Eg': 1.1, 'affinity': 0, 'epsilon': 10,
                'mu_e': 300, 'mu_h': 300, 'tau_e': tau_to_test[i], 'tau_h': tau_to_test[i], 'Et': 0}
    sys.add_material(material)
    direcc = 'C:/Users/njr3/Downloads/sesame-master/sesame-master/test1/'
    simulatin8r = sim.SimulationWorker('generation',
                                 sys, [np.linspace(2e-4,5e-4,20),
                                 direcc+'test{0}'.format(i),
                                 '.gzip', True, ['Ohmic', 'Ohmic'], ['', ''], [100000.0, 100000.0, 100000.0, 100000.0],
                                 1e-06, 100, False, False, 0, 1e-06, 1], '(1e19) * np.exp((-(x-x0)**2)/((2e-6)**2))', 'x0')
    simulatin8r.run()
    # this pops up the band diagrams, not really needed if you're going to use sesame to look at them
    for j in range(20):
        sys_load, data = utils.load_sim(direcc+'test{0}_{1}.gzip'.format(i,j))
        anal = analyzer.Analyzer(sys_load, data)
        anal.band_diagram(((0,0), (0.0006, 0)))

