import math
from random import gauss
from pyhistuples.pyntuple.ntuple import NTuple
from matplotlib import pyplot

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

x = nt.column('x', lambda row : row.p > 5. and row.pt > 1.)

