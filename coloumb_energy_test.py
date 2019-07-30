import numpy as np
import mp2 as mp2
import hartree_fock as hf
import noble_gas_model as noble_gas_model


NobleGasModel = noble_gas_model.NobleGasModl()
atomic_coordinates = np.array([[0.0,0.0,0.0], [3.0,4.0,5.0]])
hartree_fock_instance = hf.HartreeFock(NobleGasModel, atomic_coordinates)

def test_calculated_coloumb_energy():
    
   coulomb_vector = np.array([1,0,0])
   assert np.isclose (1.0, hartree_fock_instance.calculate_coloumb_energy('s','s',coulomb_vector))
   assert np.isclose (1.0, hartree_fock_instance.calculate_coloumb_energy('s','px',coulomb_vector))
   assert np.isclose (-2.0, hartree_fock_instance.calculate_coloumb_energy('px','px',coulomb_vector))
   assert np.isclose (0.0, hartree_fock_instance.calculate_coloumb_energy('s','py',coulomb_vector))
   assert np.isclose (0.0, hartree_fock_instance.calculate_coloumb_energy('px','py',coulomb_vector))
   assert np.isclose (1.0, hartree_fock_instance.calculate_coloumb_energy('py','py',coulomb_vector))

   assert np.isclose (expected_coloumb_energy, calculated_coloumb_energy)"
