'''
Test suite for histogram.axis class.
'''

__author__ = "Juan PALACIOS juan.palacios@nikhef.nl"

from random import gauss
from pyhistuples.pyntuple.ntuple import NTuple
from pyhistuples.pyhistoplots import ntuple_plot, histo_plot, ntuple_column_histo

mu_p = 15.
mu_pt = 5.
sigma_p = 10.
sigma_pt = 5.

nt = NTuple('x', 'p', 'pt')

for x in xrange(10000) :
    nt.fill('x',x)
    nt.fill('p', gauss(mu_p, sigma_p))
    nt.fill('pt', gauss(mu_pt, sigma_pt))
    nt.write()


def test_ntuple_plot() :
    pt_plot = ntuple_plot(nt, 'pt', show = False)
    p_plot = ntuple_plot(nt, 'p', errorfunction=lambda x : x.height/2., color = 'red', linewidth='1.5', show = False)


def test_ntuple_column_histo():
    h_pt = ntuple_column_histo(nt, 'pt')


def test_histo_plot() :
    h_pt = ntuple_column_histo(nt, 'pt')
    histo_plot(h_pt, color='blue', show = False)
