from ase.io import read
from ase.units import Hartree
from sparc import SPARC


def make_sparc_calc(
    atoms,
    directory,
    kpts,
    ecut_ev=500,
    spin_typ=0,
    tol_scf=1e-4,
    tol_relax=1e-3,
    d3_flag=1,
    xc='GGA_PBE',
    relax_flag=1
):
    parameters = dict(
        EXCHANGE_CORRELATION=xc,
        D3_FLAG=d3_flag,
        SPIN_TYP=spin_typ,
        KPOINT_GRID=kpts,
        ECUT=ecut_ev / Hartree,
        TOL_SCF=tol_scf,
        RELAX_FLAG=relax_flag,
        TOL_RELAX=tol_relax,
        PRINT_FORCES=1,
        PRINT_RELAXOUT=1,
        directory=directory
    )

    return SPARC(atoms=atoms, **parameters)


def run_calc(
    input_file,
    directory,
    kpts,
    output_file='converged.traj',
    energy_file='energy.txt',
    ecut_ev=500,
    spin_typ=0,
    tol_scf=1e-4,
    tol_relax=1e-3,
    d3_flag=1,
    xc='GGA_PBE',
    relax_flag=1
):
    atoms = read(input_file)

    calc = make_sparc_calc(
        atoms=atoms,
        directory=directory,
        kpts=kpts,
        ecut_ev=ecut_ev,
        spin_typ=spin_typ,
        tol_scf=tol_scf,
        tol_relax=tol_relax,
        d3_flag=d3_flag,
        xc=xc,
        relax_flag=relax_flag
    )

    atoms.calc = calc
    energy = atoms.get_potential_energy()

    atoms.write(output_file)

    with open(energy_file, 'w') as f:
        f.write(f"{energy}\n")

    print(f"{directory}: {energy:.6f} eV")
    return energy


def read_energy(path):
    with open(path, 'r') as f:
        return float(f.readline().strip())


def adsorption_energy(E_ads_system, E_clean_slab, E_gas):
    return E_ads_system - E_clean_slab - E_gas