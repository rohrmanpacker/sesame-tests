import sesame
import numpy as np

length = 6e-4  # length of the system in cm

mesh = np.linspace(0, length)

sys = sesame.Builder(mesh)



# Add the doping
nD = 1e+16
sys.add_donor(nD, lambda x: x < 3e-4)

nA = 1e+16
sys.add_acceptor(nA,lambda x: x > 3e-4)

# Define Ohmic contacts
sys.contact_type('Ohmic', 'Ohmic')

# Define the surface recombination velocities for electrons and holes [cm/s]
Sn_left, Sp_left, Sn_right, Sp_right = 1e5, 0, 0, 1e5
sys.contact_S(Sn_left, Sp_left, Sn_right, Sp_right)
tau_to_test = [1e-9,1e-8,1e-7,1e-6,1e-5]
for i in tau_to_test:
    # create the material
    material = {'Nc': 1e+19, 'Nv': 1e+19, 'Eg': 1.1, 'affinity': 0, 'epsilon': 10,
                'mu_e': 300, 'mu_h': 300, 'tau_e': tau_to_test[i], 'tau_h': tau_to_test[i], 'Et': 0}
    sys.add_material(material)
    solution = sesame.solve_equilibrium(sys)

    center = np.linspace(2e-4,5e-4,20)
    a = 1e+19
    #print(solution)
    sesame.analyzer.


def gen_func(x):
    return a * np.exp((-(x-4e-6)**2)/(2e-6**2))


#for i in range(len(center)):
sys.generation(gen_func)  # i dont think this will work



