'''
Test suite for histogram.bin class.
'''

__author__ = "Juan PALACIOS juan.palacios@nikhef.nl"

from nose import tools as nt
from pyhistuples.pyhistogram.histogram import Bin


def test_bin_contents() :
    _bin = Bin(entries=100, height=75.)
    nt.assert_true(_bin.entries == 100)
    nt.assert_true(_bin.height == 75.)
    nt.assert_true(_bin.sumWeight2 == 75.*75.)


def test_bin_addition() :
    bin0 = Bin(entries=50, height=75.)
    bin1 = Bin(entries=50, height=75.)
    bin2 = bin0+bin1
    nt.assert_true(bin2.entries == 100 and bin2.height == 150.)
    nt.assert_true(bin2.sumWeight2 == bin0.sumWeight2 + bin1.sumWeight2 == 2*pow(75.,2))


def test_bin_subtraction() :
    bin0 = Bin(entries=100, height=200.)
    bin1 = Bin(entries=50, height=75.)
    bin2 = bin0-bin1
    nt.assert_true(bin2.entries == 50 and bin2.height == 125.)
    nt.assert_true(bin2.sumWeight2 == bin0.sumWeight2 + bin1.sumWeight2)


def test_bin_division() :
    bin0 = Bin(entries=100, height=200.)
    bin1 = Bin(entries=2, height=100.)
    bin2 = bin0/bin1
    nt.assert_true(bin2.entries == 50 and bin2.height == 2.)
