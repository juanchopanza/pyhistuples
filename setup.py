#!/usr/bin/env python

from distutils.core import setup
from distutils.core import Command
from distutils import log
from distutils.command.build import build as _build
from py import test as pytest
import os

class build(_build) :
    """
    Make build command run test command.
    """
    sub_commands = _build.sub_commands + [('test', lambda self : True)]

class pytest(Command) :
    """
    Simple command to run py.test when invoking setup.py test.
    """
    
    user_options = [
        ('test-dir=', 'd', 'Which directory is the test suite located in?'),
        ('test-prefix=', 'p', 'Which do test files start with?'),
        ('stop-build=', 's', 'Stop build if tests fail'),
        ]
    def initialize_options(self):
        self.test_dir = None
        self.test_prefix = None
        self.stop_build = None

    def finalize_options(self) :
        pass

    def run(self) :
        import py.test
        tests = [os.path.join(self.test_dir,t) for t in os.listdir(self.test_dir) if t.startswith(self.test_prefix) and t.endswith('.py')]
        print 'Running tests', tests, 'stop_build', self.stop_build
        fail = py.test.cmdline.main(tests)
        if fail :
            msg = '\nERROR: py.test failure in %s/%s*.py.\n'% (self.test_dir, self.test_prefix)
            log.error(msg)
            if self.stop_build==True:
                raise Exception('Test failure: Abort build')
    # run()
    
# class pytest

setup(name='pyhistuples',
      version='0.1',
      description='Python Histogram and NTuple',
      author='Juan Palacios',
      author_email='juan.palacios.puyana@gmail.com',
      url='https://github.com/juanchopanza/pyhistuples',
      license = 'LGPL',
      long_description=open('README').read(),
      packages=['pyhistuples',
                'pyhistuples.pyhistogram',
                'pyhistuples.pyntuple'],
      requires = ['matplotlib', 'pytest'],
      cmdclass = {'test' : pytest,
                  'build' : build},
      options = { 'test' : { 'test_dir' : 'test',
                             'test_prefix' : 'test_',
                             'stop_build' : True },    }
     )
