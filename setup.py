from __future__ import print_function
try:
    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext as _build_ext
except ImportError:
    print("Please use pip (https://pypi.python.org/pypi/pip) to install.")
    raise

import os
from glob import glob
from platform import system

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
                    include_dirs = ['ecos/include',
                        'ecos/external/amd/include',
                        'ecos/external/ldl/include',
                        'ecos/external/SuiteSparse_config'],
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

def set_builtin(name, value):
    if isinstance(__builtins__, dict):
        __builtins__[name] = value
    else:
        setattr(__builtins__, name, value)

class build_ext(_build_ext):
    """ This custom class for building extensions exists so we can force
    a numpy install before building the extension, thereby giving us
    access to the numpy headers.
    """
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        set_builtin("__NUMPY_SETUP__", False)
        import numpy
        self.include_dirs.append(numpy.get_include())

setup(
    name = 'ecos',
    version = '2.0.12',
    author = 'Alexander Domahidi, Eric Chu, Han Wang, Santiago Akle',
    author_email = 'domahidi@embotech.com, echu@cs.stanford.edu, hanwang2@stanford.edu, tiagoakle@gmail.com',
    url = 'http://github.com/embotech/ecos',
    description = 'This is the Python package for ECOS: Embedded Cone Solver. See Github page for more information.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license = "GPLv3",
    packages = ['ecos'],
    package_dir = {'': 'src'},
    cmdclass = {'build_ext': build_ext},
    ext_modules = [_ecos],
    setup_requires = [
        "numpy >= 1.6"
    ],
    install_requires = [
        "numpy >= 1.6",
        "scipy >= 0.9"
    ],
    test_suite='nose.collector',
    tests_require=['nose']
)
