'''
Test suite for histogram.bin class.
'''

__author__ = "Juan PALACIOS juan.palacios@nikhef.nl"

import sys, os
sys.path.append(os.path.abspath('..'))

from pyhistuples.pyhistogram.histogram import Bin

def test_bin_contents() :
    bin = Bin(entries = 100, height = 75.)
    assert bin.entries == 100
    assert bin.height == 75.
    assert bin.sumWeight2 == 75.*75.
    
def test_bin_addition() :
    bin0 = Bin(entries = 50, height = 75.)
    bin1 = Bin(entries = 50, height = 75.)
    bin2 = bin0+bin1
    assert bin2.entries == 100 and bin2.height == 150.
    assert bin2.sumWeight2 == bin0.sumWeight2 + bin1.sumWeight2 == 2*pow(75.,2)
    
def test_bin_subtraction() :
    bin0 = Bin(entries = 100, height = 200.)
    bin1 = Bin(entries = 50, height = 75.)
    bin2 = bin0-bin1
    assert bin2.entries == 50 and bin2.height == 125.
    assert bin2.sumWeight2 == bin0.sumWeight2 + bin1.sumWeight2
    
def test_bin_division() :
    bin0 = Bin(entries = 100, height = 200.)
    bin1 = Bin(entries = 2, height = 100.)
    bin2 = bin0/bin1
    assert bin2.entries == 50 and bin2.height == 2.
