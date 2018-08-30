from __future__ import print_function
try:
    from setuptools import setup, Extension
except ImportError:
    print("Please use pip (https://pypi.python.org/pypi/pip) to install.")
    raise

from glob import glob
from platform import system

lib = []
if system() == 'Linux':
    lib += ['rt']

class CustomExtension(Extension, object):
    def __getattribute__(self, attr):
        if attr == "include_dirs":
            import numpy
            return  ['ecos/include', numpy.get_include(),
                     'ecos/external/amd/include',
                     'ecos/external/ldl/include',
                     'ecos/external/SuiteSparse_config']
        else:
            return super(CustomExtension, self).__getattribute__(attr)

_ecos = CustomExtension('_ecos', libraries = lib,
                    # define LDL and AMD to use long ints
                    # also define that we are building a python module
                    define_macros = [
                        ('PYTHON',None),
                        ('DLONG', None),
                        ('LDL_LONG', None),
                        ('CTRLC', 1)],
                    sources = ['src/ecosmodule.c',
                        'ecos/external/ldl/src/ldl.c',
                        'ecos/src/cone.c',
                        'ecos/src/ctrlc.c',
                        'ecos/src/ecos.c',
                        'ecos/src/equil.c',
                        'ecos/src/expcone.c',
                        'ecos/src/kkt.c',
                        'ecos/src/preproc.c',
                        'ecos/src/spla.c',
                        'ecos/src/splamm.c',
                        'ecos/src/timer.c',
                        'ecos/src/wright_omega.c'
                    ] + glob('ecos/external/amd/src/*.c')
                      + glob('ecos/ecos_bb/*.c'))       # glob bb source files

setup(
    name = 'ecos',
    version = '2.0.5',  # read from ecos submodule
    # point to README.md file instead of plain-text readme
    author = 'Alexander Domahidi, Eric Chu, Han Wang, Santiago Akle',
    author_email = 'domahidi@embotech.com, echu@cs.stanford.edu, hanwang2@stanford.edu, tiagoakle@gmail.com',
    url = 'http://github.com/embotech/ecos',
    description = 'This is the Python package for ECOS: Embedded Cone Solver. See Github page for more information.',
    license = "GPLv3",
    package_dir = {'': 'src'},
    py_modules = ['ecos'],
    ext_modules = [_ecos],
    setup_requires = [
        "numpy >= 1.6",
    ],
    install_requires = [
        "numpy >= 1.6",
        "scipy >= 0.9"
    ]
)
