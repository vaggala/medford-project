import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, PROJECT_ROOT)

from scripts.calc_sparc import run_calc

run_calc(
    input_file='pt111_atop.traj',
    directory='pt111_atop_sparc',
    kpts=[2, 2, 1],
    output_file='converged.traj',
    energy_file='energy.txt',
    d3_flag=0,
    spin_typ=0,
    relax_flag=1
)