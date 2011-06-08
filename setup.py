#!/usr/bin/env python

from distutils.core import setup

setup(name='Pyhistuples',
      version='1.0',
      description='Python Histogram and NTuple',
      author='Juan Palacios',
      author_email='juan.palacios.puyana@gmail.com',
      url='https://github.com/juanchopanza/pyhistuples',
      license = 'LGPL',
      packages=['pyhistuples',
                'pyhistuples.pyhistogram',
                'pyhistuples.pyntuple'],
      requires = ['matplotlib', 'pytest'],
     )
