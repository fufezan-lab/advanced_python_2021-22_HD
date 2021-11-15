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

def test_proteins_find_metric_values():
    test_protein = proteins.basic.Protein("Test_Name", "AR")
    metric_values = test_protein.find_metric_values()
    assert metric_values == [1.8, -4.5]

def test_proteins_calculate_sliding_window():
    test_protein = proteins.basic.Protein("Test_Name", "ARARA")
    mean_value = test_protein.calculate_sliding_window()
    assert mean_value == [1.8, -1.35, -0.30000000000000004, -1.35, -0.7200000000000001]

def test_proteins_create_positions():
    test_protein = proteins.basic.Protein("Test_Name", "ARARA")
    pos = test_protein.create_positions()
    assert pos == [0, 1, 2, 3, 4]
