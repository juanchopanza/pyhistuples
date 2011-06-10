import math
from random import gauss
from pyhistuples.pyntuple.ntuple import NTuple
from matplotlib import pyplot
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


pt_plot = ntuple_plot(nt, 'pt')
h_pt = ntuple_column_histo(nt, 'pt')
histo_plot(h_pt, color='blue')
