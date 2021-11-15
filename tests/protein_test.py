import sys
from pathlib import Path
# -------- START of inconvenient addon block --------
# This block is not necessary if you have installed your package
# using e.g. pip install -e (requires setup.py)
# or have a symbolic link in your sitepackages (my preferend way)
sys.path.append(
    str(Path(__file__).parent.parent.resolve())
)
# It make import peak_finder possible
# This is a demo hack for the course :)
# --------  END of inconvenient addon block  --------

import proteins

# Name
# Sequenz
# Plot Methode

def test_proteins_name():
    test_protein = proteins.basic.Protein("Test_Name", "AAAAA")
    name_test = test_protein.name
    assert name_test == "Test_Name"


def test_proteins_sequence():
    test_protein = proteins.basic.Protein("Test_Name", "AAAAA")
    seq = test_protein.sequence
    assert seq == "AAAAA"

def test_proteins_plot():
    test_protein = proteins.basic.Protein("Test_Name", "AAAAA")

