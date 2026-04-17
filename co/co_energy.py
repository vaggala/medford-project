import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from scripts.calc_sparc import run_calc

run_calc(
    input_file='co.traj',
    directory='co_sparc',
    kpts=[1, 1, 1],
    output_file='converged.traj',
    energy_file='energy.txt',
    d3_flag=0,
    spin_typ=0,
    relax_flag=0,
    tol_scf=1e-5
)