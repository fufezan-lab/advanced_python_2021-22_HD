import sys
from pathlib import Path
import numpy as np
import unittest
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

from protein_object.protein_basic import Protein

def test_file_load():
    protein = Protein("P32249.fasta")

    assert not protein is None

def test_protein_length():
    protein = Protein("P32249.fasta")
    protein_length = len(protein.get_property_list())
    assert protein_length == 361

def test_protein_length_0():
    protein = Protein("0_test.fasta")
    protein_length = len(protein.get_property_list())
    assert protein_length == 0

def test_protein_length_1():
    protein = Protein("1_test.fasta")
    protein_length = len(protein.get_property_list())
    assert protein_length == 1

def test_protein_list_0():
    protein = Protein("0_test.fasta")
    protein_list = protein.get_property_list()
    assert protein_list == []

def test_protein_list_1():
    protein = Protein("1_test.fasta")
    protein_list = protein.get_property_list()
    with open("error.txt", 'w') as error_log:
        error_log.write("WtestW")
        error_log.write("\n")
        error_log.write(str(protein_list))
        error_log.write("\n")
        error_log.write(str(len(protein.get_property_list())))
    assert protein_list == [1.9]


def test_protein_list_MGÖÄL():
    try:
        protein = Protein("MGÖÄL_test copy.fasta")
        protein_list = protein.get_property_list()
    except UnicodeDecodeError:
        test_worked = True
    else: 
        test_worked = False
    '''with open("error.txt", 'w') as error_log:
        error_log.write("WtestW")
        error_log.write("\n")
        error_log.write(str(protein_list))
        error_log.write("\n")
        error_log.write(str(len(protein.get_property_list())))'''
    assert test_worked == True



def test_protein_plot_1():
    protein = Protein("1_test.fasta")
    plot = protein.plot()
    plot.show()
    assert not plot is None