import sesame
from sesame.ui import sim
from sesame import analyzer,utils,builder
import numpy as np
import random

length = 6e-4  # length of the system in cm

pop_up_spam = False # if you want the band diagrams to pop up
# this is the directory where the files will go
direcc = 'C:/Users/njr3/Downloads/sesame-master/sesame-master/test1/'

mesh = np.linspace(0, length)
# doping amounts [1/cm^3]
nD = 1e+16
nA = 1e+16

#tau values to iterate through
tau_to_test = [1e-9,1e-8,1e-7,1e-6,1e-5]
#center values to iterate through
center = np.linspace(2e-4,5e-4,20)

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
    simulatin8r = sim.SimulationWorker('generation',
                                 sys, [np.linspace(2e-4,5e-4,20),
                                 direcc+f'test{i}',
                                 '.gzip', True, ['Ohmic', 'Ohmic'], ['', ''], [100000.0, 100000.0, 100000.0, 100000.0],
                                 1e-06, 100, False, False, 0, 1e-06, 1], '(1e19) * np.exp((-(x-x0)**2)/((2e-6)**2))', 'x0')
    simulatin8r.run()
    # this pops up the band diagrams, not really needed if you're going to use sesame to look at them
    if pop_up_spam:
        for j in range(20):
            sys_load, data = utils.load_sim(direcc+f'test{i}_{j}.gzip')
            anal = analyzer.Analyzer(sys_load, data)
            anal.band_diagram(((0, 0), (0.0006, 0)))

