from scripts.calc_sparc import read_energy, adsorption_energy
    
E_co = read_energy("../co/energy.txt")
E_clean = read_energy("clean/energy.txt")
E_atop = read_energy("atop/energy.txt")
E_fcc = read_energy("fcc/energy.txt")

E_ads_atop = E_atop - E_clean - E_co
E_ads_fcc = E_fcc - E_clean - E_co

Eads_atop = adsorption_energy(E_atop, E_clean, E_co)
Eads_fcc = adsorption_energy(E_fcc, E_clean, E_co)

print(f"E_clean = {E_clean:.6f} eV")
print(f"E_atop  = {E_atop:.6f} eV")
print(f"E_fcc   = {E_fcc:.6f} eV")
print(f"E_CO    = {E_co:.6f} eV\n")
print(f"Atop adsorption energy = {Eads_atop:.6f} eV")
print(f"FCC adsorption energy  = {Eads_fcc:.6f} eV")