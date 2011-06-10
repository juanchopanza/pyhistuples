import math
from random import gauss, expovariate
from matplotlib import pyplot
from scipy import optimize, arange

from pyhistuples.pyhistoplots import histo_plot
from pyhistuples.pyhistogram.histogram import Histogram, Axis


def gaussian(mu, sigma2, x) :
    norm = math.sqrt( 2*math.pi*sigma2 )
    exponent = -1*pow(x-mu,2)/(2*sigma2 )
    return math.exp(exponent)/norm

def fitfunc(params,xx) :
    return [params[2]*gaussian(params[0], params[1], x) for x in xx]

class ErrFunc(object) :
    def __init__(self, histogram, fitfunc) :
        self.fitfunc=fitfunc
        bins =  histogram.filledBins()
        self.x = [bin.centre for bin in bins]
        self.y = [bin.height for bin in bins]
    def __call__(self, params) :
        return  map(lambda g, e : g-e, fitfunc(params, self.x), self.y)

mu_pt = 5.
sigma_pt = 15.
sigma2_pt=pow(sigma_pt,2)

h_pt = Histogram(axis=Axis(100, -50, 50, label='pt'))

for i in xrange(10000) :
    h_pt.fill(gauss(mu_pt, sigma_pt))

p0 = [15., 10, 1000.] # mu, sigma, integral.

errfunc = ErrFunc(h_pt, fitfunc)

p0, success = optimize.leastsq(errfunc,
                               p0[:])

print 'Success:', success, 'p[0] =', p0[0], ' p[1] =', p0[1], ' p0[2] =', p0[2]

plot_pt = histo_plot(h_pt, color='green')

# plot the fit results on top.
fit=plot_pt.add_subplot(1,1,1)
pt = [bin.centre for bin in h_pt.filledBins()]
fitval = fitfunc(p0,pt)
fit.plot(pt, fitval, 'r')

plot_pt.show()
