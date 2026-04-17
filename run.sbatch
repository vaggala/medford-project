#!/bin/bash
# SBATCH --job-name=co_adsorption
# SBATCH --output=logs/%x_%j.out
# SBATCH --error=logs/%x_%j.err
# SBATCH --time=04:00:00
# SBATCH --nodes=1
# SBATCH --ntasks=1
# SBATCH --cpus-per-task=8
# SBATCH --mem=8G

# comment in/out lines as needed.

echo "Starting job at $(date)"

# Load environment
source ~/scratch/interact.sh
source ~/packages/sparc_env.sh

cd ~/scratch/medford_project

########################################
# CO calculation
########################################
# echo "Running CO calculation..."
# cd co
# python build_co.py
# python co_energy.py
# cd ..

# ########################################
# # PT(111) calculations
# ########################################
# echo "Running Pt(111) calculations..."

# # Clean
# cd pt111/clean
# python build_pt111.py
# python clean_energy.py
# cd ../..

# # Atop
# cd pt111/atop
# python build_pt111_atop.py
# python atop_energy.py
# cd ../..

# # FCC Hollow
# cd pt111/fcc_hollow
# python build_pt111_fcc_hollow.py
# python fcc_hollow_energy.py
# cd ../..

# Analysis
cd pt111
python pt111_analysis.py
cd ..

########################################
# CU(111) calculations
########################################
echo "Running Cu(111) calculations..."

# Clean
# cd cu111/clean
# python build_cu111.py
# python clean_energy.py
# cd ../..

# # Atop
# cd cu111/atop
# python build_cu111_atop.py
# python atop_energy.py
# cd ../..

# # FCC Hollow
# cd cu111/fcc_hollow
# python build_cu111_fcc_hollow.py
# python fcc_hollow_energy.py
# cd ../..

# Analysis
cd cu111
python cu111_analysis.py
cd ..

echo "Job finished at $(date)"