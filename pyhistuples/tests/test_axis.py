'''
Test suite for histogram.axis class.
'''

__author__ = "Juan PALACIOS juan.palacios@nikhef.nl"

from nose import tools as nt
from pyhistuples.pyhistogram.histogram import Axis


def test_instantiate_axis() :
    ax = Axis(100, -50, 50, "My first axis")
    nt.assert_true(ax is not None)


def test_axis_parameters() :
    ax = Axis(100, -50, 50, "My first axis")
    nt.assert_true(ax.nbins == 100)
    nt.assert_true(ax.min == -50.)
    nt.assert_true(ax.max == 50.)
    nt.assert_true(ax.label == "My first axis")
    nt.assert_true(ax.range == (-50,50))


def test_axis_bin_width() :
    ax = Axis(100, -50, 50, "My first axis")
    nt.assert_true(ax.binWidth() == 1.)


def test_axis_bin_centre() :
    ax = Axis(20, -10, 10, "My first axis")
    reference = [x+0.5 for x in xrange(-10,10)]
    for i in xrange(10) :
        nt.assert_true(ax.binCentre(i) == reference[i])


@nt.raises(IndexError)
def test_invalid_bin_center_raises_IndexError() :
    ax = Axis(20, -10, 10, "My first axis")
    ax.binCentre(max(ax.underflow_bin, ax.overflow_bin)+1)


def test_invalid_range_gets_special_bins() :
    ax = Axis(20, -10, 10, "My first axis")
    nt.assert_true(ax.binIndex(11) == ax.overflow_bin)
    nt.assert_true(ax.binIndex(-11) == ax.underflow_bin)


def test_axis_equality() :
    ax0 = Axis(20, -10, 10, "My first axis")
    ax1 = Axis(20, -10, 10, "My first axis")
    nt.assert_true(ax0==ax1)


def test_axis_inequality() :
    ax0 = Axis(20, -10, 10, "My first axis")
    ax1 = Axis(30, -10, 10, "My first axis")
    nt.assert_true(ax0!=ax1)


def test_compare_to_Nonsense() :
    ax0 = Axis(20, -10, 10, "My first axis")
    nt.assert_true(ax0 is not None)
    nt.assert_true(not ax0 is None)
    nt.assert_true(ax0 != 1)
    nt.assert_true(ax0 !=5.0)
    nt.assert_true(ax0 != [])
