#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path
from datetime import datetime

# === Step 1: Define Paths ===
RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
RESULTS_DIR = Path("results")
FIGURES_DIR = RESULTS_DIR / "figures"
NOTEBOOKS_DIR = Path("notebooks")

# === Step 2: Create Necessary Directories ===
for d in [PROCESSED_DIR, FIGURES_DIR, RESULTS_DIR / "ARG"]:
    d.mkdir(parents=True, exist_ok=True)

# === Step 3: Utility Function ===
def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# === Step 4: Run Notebooks Sequentially ===
notebooks = [
    "01_qc_trimming.ipynb",
    "02_taxonomy.ipynb",
    "03_ARG_annotation.ipynb",
    "04_visualization.ipynb"
]

def run_notebook(nb_name):
    log(f"Running {nb_name} ...")
    cmd = [
        "jupyter", "nbconvert", "--to", "notebook", "--execute",
        "--inplace", str(NOTEBOOKS_DIR / nb_name)
    ]
    subprocess.run(cmd, check=True)

# === Step 5: Pipeline Run ===
def main():
    log("🧪 Starting Metagenomics ARG Profiling Pipeline...")
    
    for nb in notebooks:
        run_notebook(nb)

    log("✅ Pipeline completed successfully.")
    log(f"📁 All results are in: {RESULTS_DIR.resolve()}")
    log(f"📊 Figures saved in: {FIGURES_DIR.resolve()}")

if __name__ == "__main__":
    main()
