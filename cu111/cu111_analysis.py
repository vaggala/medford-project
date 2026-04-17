import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from scripts.calc_sparc import read_energy, adsorption_energy
    
E_co = read_energy("../co/energy.txt")
E_clean = read_energy("clean/energy.txt")
E_atop = read_energy("atop/energy.txt")
E_fcc = read_energy("fcc_hollow/energy.txt")

# Compute adsorption energies
Eads_atop = adsorption_energy(E_atop, E_clean, E_co)
Eads_fcc = adsorption_energy(E_fcc, E_clean, E_co)

print(f"E_clean = {E_clean:.6f} eV")
print(f"E_atop  = {E_atop:.6f} eV")
print(f"E_fcc   = {E_fcc:.6f} eV")
print(f"E_CO    = {E_co:.6f} eV\n")

print(f"Atop adsorption energy = {Eads_atop:.6f} eV")
print(f"FCC adsorption energy  = {Eads_fcc:.6f} eV\n")

diff = Eads_fcc - Eads_atop

if diff < 0:
    print(f"DFT predicts that the FCC site for Cu(111) is more stable than the atop site by {abs(diff):.3f} eV")
else:
    print(f"DFT predicts that the atop site for Cu(111) is more stable than the FCC site by {abs(diff):.3f} eV")

print("Compare this with literature values for CO adsorption on Cu(111).")