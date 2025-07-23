![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

# Metagenomic Profiling of Antibiotic Resistance Genes

This project explores antibiotic resistance genes (ARGs) in human gut microbiomes using publicly available shotgun metagenomic sequencing data. It applies tools like **Kraken2**, **Bracken**, and **DeepARG** for resistome and taxonomic profiling.

---

## 📑 Table of Contents

- [Objectives](#objectives)
- [Pipeline Steps]
- [Visual Outputs]
- [Tools & Frameworks]
- [Results](#results)
- [How to Cite](#how-to-cite)
- [License](#license)

---

## 🎯 Objectives

- Taxonomic profiling of human gut microbiota
- Annotation of antibiotic resistance genes
- Visualization of ARG class distribution and species composition

---


---

## 🔬 Pipeline Steps

| Step | Description |
|------|-------------|
| **01. Quality Control & Trimming** | Adapter removal and read trimming using `fastp` |
| **02. Taxonomic Profiling**        | Classification using `Kraken2` with visualizations |
| **03. ARG Annotation**             | Detection of resistance genes using `RGI` and CARD |
| **04. Visualization**              | Heatmaps, barplots, and pie charts in Python |

Each notebook is modular and reproducible.

---

## 📊 Visual Outputs

- **Bar plots** showing ARG abundance per sample
- **Pie charts** for gene class distribution
- **Heatmaps** representing resistance gene frequency across samples

> All outputs are stored in `/results/figures/`

---

## 🧪 Tools & Frameworks

- `Fastp` (QC)
- `Kraken2` (Taxonomy)
- `RGI` (Resistance annotation)
- `Pandas`, `Seaborn`, `Matplotlib` (Plotting)
- `Biopython` (Sequence handling)
- `Python ≥ 3.9`, `Conda` (Environment)



```

## 📊 Results
Output files include:

Taxonomic composition per sample

ARG annotations with class and identity

Visual plots in results/figures/

🤝 Acknowledgments
This pipeline was designed as part of a self-initiated research and coding project by Subhadip Jana, focused on environmental bioinformatics and AMR surveillance.

## 📖 How to Cite

If you use this pipeline in your work, please cite:
Subhadip Jana (2025).
Metagenomic Profiling of Antibiotic Resistance Genes.
GitHub Repository: https://github.com/SubhadipJana1409/metagenomics-arg


## 🪪 License

This project is licensed under the MIT License. See LICENSE for details.

Copyright (c) 2025 Subhadip Jana

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
