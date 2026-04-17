#!/bin/bash

# placeholder file

module load intel/2021.9.0
module load intel-oneapi-mkl/2023.1.0
module load mvapich2
module load anaconda3

conda activate sparc

export PATH=export PATH=/path/to/SPARC/lib
export SPARC_PSP_PATH=/path/to/SPARC/psps

# if [[ -z "${SLURM_NTASKS}" ]]; then
#     export ASE_SPARC_COMMAND="/home/hice1/vaggala3/scratch/SPARC/lib/sparc -name PREFIX"
# else
#     export ASE_SPARC_COMMAND="srun /home/hice1/vaggala3/scratch/SPARC/lib/sparc -name PREFIX"
# fi

export ASE_SPARC_COMMAND="srun /path/to/SPARC/lib/sparc"