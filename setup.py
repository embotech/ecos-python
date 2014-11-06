from __future__ import print_function
try:
    from setuptools import setup, Extension
except ImportError:
    print("Please use pip (https://pypi.python.org/pypi/pip) to install.")
    raise

from glob import glob
from platform import system
import numpy

lib = []
if system() == 'Linux':
    lib += ['rt']

_ecos = Extension('_ecos', libraries = lib,
                    # define LDL and AMD to use long ints
                    # also define that we are building a python module
                    define_macros = [
                        ('PYTHON',None),
                        ('DLONG', None),
                        ('LDL_LONG', None),
                        ('CTRLC', 1)],
                    include_dirs = ['ecos/include', numpy.get_include(),
                        'ecos/external/amd/include',
                        'ecos/external/ldl/include',
                        'ecos/external/SuiteSparse_config'],
                    sources = ['src/ecosmodule.c',
                        'ecos/external/ldl/src/ldl.c'
                    ] + glob('ecos/external/amd/src/*.c')
                      + glob('ecos/src/*.c')            # glob source files
                      + glob('ecos/ecos_bb/*.c'))       # glob bb source files

setup(
    name = 'ecos',
    version = '1.1.0',  # read from ecos submodule
    # point to README.md file instead of plain-text readme
    author = 'Alexander Domahidi, Eric Chu, Han Wang',
    author_email = 'domahidi@embotech.com, echu@cs.stanford.edu, hanwang2@stanford.edu',
    url = 'http://github.com/embotech/ecos',
    description = 'This is the Python package for ECOS: Embedded Cone Solver. See Github page for more information.',
    license = "GPLv3",
    py_modules = ['ecos'],
    ext_modules = [_ecos],
    install_requires = [
        "numpy >= 1.6",
        "scipy >= 0.9"
    ]
)
