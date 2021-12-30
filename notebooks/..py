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
import pytest
from peak_finder.basic import find_peaks

def test_find_peaks():
    peaks = find_peaks([0, 2, 1])
    assert peaks == [2] 

def test_left_rand_is_peak():
    peaks = find_peaks([7, 2, 1])
    assert peaks == [7] 

def test_right_rand_is_peak():
    peaks = find_peaks([0, 2, 6])
    assert peaks == [6] 

def test_both_rand_is_peak():
    peaks = find_peaks([8, 2, 6])
    assert peaks == [8, 6] 

def test_all_touple():
    peaks = find_peaks([(8,2), "2", (6,5)])
    assert peaks == []

def test_all_int():
    peaks = find_peaks([2, 2, (6,5)])
    assert peaks == []

#repeat for tuples
def test_find_peaks_tuple():
    peaks = find_peaks([(0,4), (2,8), (1,7)])
    assert peaks == [(2,8)] 

def test_left_rand_is_peak_tuple():
    peaks = find_peaks([(2,8), (1,7), (0,4)])
    assert peaks == [(2,8)] 

def test_right_rand_is_peak_tuple():
    peaks = find_peaks([(0,4), (1,7), (2,8)])
    assert peaks == [(2,8)] 

def test_both_rand_is_peak_tuple():
    peaks = find_peaks([(2,8), (0,4), (1,7)])
    assert peaks == [(2,8), (1,7)] 
