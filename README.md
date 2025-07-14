![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

# Metagenomic Profiling of Antibiotic Resistance Genes

This project explores antibiotic resistance genes (ARGs) in human gut microbiomes using publicly available shotgun metagenomic sequencing data. It applies tools like **Kraken2**, **Bracken**, and **DeepARG** for resistome and taxonomic profiling.

---

## 📑 Table of Contents

- [Objectives](#objectives)
- [Directory Structure](#directory-structure)
- [Tools Used](#tools-used)
- [Usage](#usage)
- [Results](#results)
- [How to Cite](#how-to-cite)
- [License](#license)

---

## 🎯 Objectives

- Taxonomic profiling of human gut microbiota
- Annotation of antibiotic resistance genes
- Visualization of ARG class distribution and species composition

---

## 🗂️ Directory Structure

├── data/
│ ├── raw/
│ └── processed/
├── notebooks/
├── env/
├── results/
│ └── figures/
├── README.md
├── run_pipeline.py
└── LICENSE

---

## 🛠️ Tools Used

- `fastp`, `sra-tools`, `Kraken2`, `Bracken`, `DeepARG`
- `Bowtie2` for alignment
- `Python`, `JupyterLab`, `Seaborn`, `Matplotlib`

---

## 🚀 Usage

```bash
# Create conda environment
conda env create -f env/environment.yml
conda activate metagenomics-arg

# Run the pipeline
python run_pipeline.py
```

📊 Results
Output files include:

Taxonomic composition per sample

ARG annotations with class and identity

Visual plots in results/figures/

If you use this pipeline in your work, please cite:

Subhadip Jana (2025).
Metagenomic Profiling of Antibiotic Resistance Genes.
GitHub Repository: https://github.com/SubhadipJana1409/metagenomics-arg


🪪 License
This project is licensed under the MIT License. See LICENSE for details.