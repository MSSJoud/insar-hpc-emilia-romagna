#!/bin/bash
#!/bin/bash
#SBATCH --job-name=insar_cuda_strong
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --partition=gpu
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err

module load cuda/12.0  # adapt to Strato
# activate your conda env
source ~/miniconda3/etc/profile.d/conda.sh
conda activate insar_cuda

srun python pipeline/driver_run_isce3_cuda.py \
    --config configs/config_insar_cuda.yaml
