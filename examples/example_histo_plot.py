import math
from random import gauss
from pyhistuples.pyntuple.ntuple import NTuple
from matplotlib import pyplot
from pyhistuples.pyhistoplots import ntuple_plot, histo_plot, ntuple_column_histo
from pyhistuples.pyhistogram.histogram import Histogram, Axis

mu_p = 15.
mu_pt = 5.
sigma_p = 10.
sigma_pt = 5.

nt = NTuple('x', 'p', 'pt')

h_pt = Histogram(axis=Axis(100, -50, 50, label='pt'))

for x in xrange(10000) :
    val = gauss(mu_pt, sigma_pt)
    h_pt.fill(val)

# greem plot without errors
plot_pt = histo_plot(h_pt, color='green', errorfunction=None)

# blue plot with default errors (poissonSigma)
plot_pt_errors = histo_plot(h_pt, color='blue')

print 'plot_pt range', plot_pt.axes[0].xaxis.get_view_interval()

print 'plot_pt_errors range', plot_pt_errors.axes[0].xaxis.get_view_interval()
