# XAI labs

Everything you need is in the notebooks: the instructions, the questions, hints,
starter code and cells for your answers.

## Setup
    pip install -r requirements.txt
    jupyter notebook

Keep all files in this folder together: the notebooks import `xai_lab_utils.py`.

## Contents
- `Lab1_Intrinsic_Models.ipynb`
- `Lab2_Model_Agnostic_Methods.ipynb`
- `Lab3_Deep_Learning.ipynb`
- `xai_lab_utils.py` - helper functions (group seed, data file, your patient, Lab 3 settings, small CNN)
- `data/` - `heart_group_XX.csv` (one per group) and `heart_original.csv`
- `images/` - images for Lab 3
- `mystery_models/` - models for the Advanced question in Lab 3

## Before you start
Set `GROUP_NUMBER` in the first code cell of each notebook.
Lab 3 downloads the pretrained ResNet-50, MNIST and Fashion-MNIST the first time it runs.
Hand in each notebook with all cells run.
