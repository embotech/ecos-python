# Python Wrapper for Embedded Conic Solver (ECOS)

[![Build Status](https://travis-ci.org/embotech/ecos-python.svg?branch=master)](https://travis-ci.org/embotech/ecos-python)
[![Build Status](https://ci.appveyor.com/api/projects/status/78aatn417av1ul5u?svg=true)](https://ci.appveyor.com/project/echu/ecos-python)

**Visit www.embotech.com/ECOS for detailed information on ECOS.**

ECOS is a numerical software for solving convex second-order cone
programs (SOCPs) of type
```
min  c'*x
s.t. A*x = b
     G*x <=_K h
```
where the last inequality is generalized, i.e. `h - G*x` belongs to the
cone `K`. ECOS supports the positive orthant `R_+` and second-order
cones `Q_n` defined as
```
Q_n = { (t,x) | t >= || x ||_2 }
```
In the definition above, t is a scalar and `x` is in `R_{n-1}`. The cone
`K` is therefore a direct product of the positive orthant and
second-order cones:
```
K = R_+ x Q_n1 x ... x Q_nN
```

## Installation
The latest version of ECOS is available via `pip`:

    pip install ecos

This will download the relevant wheel for your machine.

### Building from source
If you are attempting to build the Python extension from source, then
use

    make install

This will use the latest tag on git to version your local installation
of ECOS.

You will need [Numpy](http://www.numpy.org/)
and [Scipy](http://www.scipy.org/). For installation instructions, see
their respective pages.

You may need `sudo` privileges for a global installation.

### Windows users
Windows users may experience some extreme pain when installing ECOS from
source for Python 2.7. We suggest switching to Linux or Mac OSX.

If you must use (or insist on using) Windows, we suggest using
the [Miniconda](http://repo.continuum.io/miniconda/)
distribution to minimize this pain.

If during the installation process, you see the error message
`Unable to find vcvarsall.bat`, you will need to install
[Microsoft Visual Studio Express 2008](go.microsoft.com/?linkid=7729279),
since *Python 2.7* is built against the 2008 compiler.

If using a newer version of Python, you can use a newer version of
Visual Studio. For instance, Python 3.3 is built against [Visual Studio
2010](http://go.microsoft.com/?linkid=9709949).

## Calling ECOS from Python

After installing the ECOS interface, you must import the module with
```
import ecos
```
This module provides a single function `ecos` with one of the following calling sequences:
```
solution = ecos.solve(c,G,h,dims)
solution = ecos.solve(c,G,h,dims,A,b,**kwargs)
```
The arguments `c`, `h`, and `b` are Numpy arrays (i.e., matrices with a single
column).  The arguments `G` and `A` are Scipy *sparse* matrices in CSR format;
if they are not of the proper format, ECOS will attempt to convert them.  The
argument `dims` is a dictionary with two fields, `dims['l']` and `dims['q']`.
These are the same fields as in the Matlab case. If the fields are omitted or
empty, they default to 0.
The argument `kwargs` can include the keywords
+ `feastol`, `abstol`, `reltol`, `feastol_inacc`, `abstol_innac`, and `reltol_inacc` for tolerance values,
+ `max_iters` for the maximum number of iterations,
+ the Booleans `verbose` and `mi_verbose`,
+ `bool_vars_idx`, a list of `int`s which index the boolean variables,
+ `int_vars_idx`, a list of `int`s which index the integer variables,
+ `mi_max_iters` for maximum number of branch and bound iterations (mixed integer problems only),
+ `mi_abs_eps` for the absolute tolerance between upper and lower bounds (mixed integer problems only), and
+ `mi_rel_eps` for the relative tolerance, (U-L)/L, between upper and lower bounds (mixed integer problems only).

The arguments `A`, `b`, and `kwargs` are optional.

The returned object is a dictionary containing the fields `solution['x']`, `solution['y']`, `solution['s']`, `solution['z']`, and `solution['info']`.
The first four are Numpy arrays containing the relevant solution. The last field contains a dictionary with the same fields as the `info` struct in the MATLAB interface.

## Using ECOS with CVXPY

[CVXPY](http://cvxpy.org) is a powerful Python modeling framework for
convex optimization, similar to the MATLAB counterpart CVX. ECOS is one
of the default solvers in CVXPY, so there is nothing special you have to
do in order to use ECOS with CVXPY, besides specifying it as a solver.
Here is a small
[example](http://www.cvxpy.org/en/latest/tutorial/advanced/index.html#solve-method-options)
from the CVXPY tutorial:

```
# Solving a problem with different solvers.
x = Variable(2)
obj = Minimize(norm(x, 2) + norm(x, 1))
constraints = [x >= 2]
prob = Problem(obj, constraints)

# Solve with ECOS.
prob.solve(solver=ECOS)
print "optimal value with ECOS:", prob.value
```

## ECOS Versioning
The Python module contains two version numbers:

1. `ecos.__version__`: This is the version of the Python wrapper for
   ECOS
2. `ecos__solver_version__`: This is the version of the underlying ECOS
   solver

These two version numbers should typically agree, but they might not
when a bug in the Python module has been fixed and nothing in the
underlying C solver has changed. The major version numbers should agree,
however.

### What happened to 2.0.7?
Because version-syncing ECOS and ECOS-Python can be tricky, the 2.0.7
version did not incorporate some minor changes to ECOS. In an
ill-advised move, the release was deleted in hopes it could be
re-uploaded, despite plenty warnings stating otherwise.

Instead, a post release has been made that contains identical content to
the 2.0.7 release. Generally, `pip` should pick up the post release for
2.0.7 and any dependencies such as `pip install "ecos>=2.0.5"` should still
work as expected.

## License

ECOS is distributed under the [GNU General Public License
v3.0](http://www.gnu.org/copyleft/gpl.html). Other licenses may be
available upon request from [embotech](http://www.embotech.com).




## Credits

The solver is essentially based on Lieven Vandenberghe's [CVXOPT](http://cvxopt.org) [ConeLP](http://www.ee.ucla.edu/~vandenbe/publications/coneprog.pdf) solver, although it differs in the particular way the linear systems are treated.

The following people have been, and are, involved in the development and maintenance of ECOS:

+ Alexander Domahidi (principal developer)
+ Eric Chu (Python interface, unit tests)
+ Stephen Boyd (methods and maths)
+ Michael Grant (CVX interface)
+ Johan Löfberg (YALMIP interface)
+ João Felipe Santos, Iain Dunning (Julia interface)
+ Han Wang (ECOS branch and bound)

The main technical idea behind ECOS is described in a short [paper](http://www.stanford.edu/~boyd/papers/ecos.html). More details are given in Alexander Domahidi's [PhD Thesis](http://e-collection.library.ethz.ch/view/eth:7611?q=domahidi) in Chapter 9.

If you find ECOS useful, you can cite it using the following BibTex entry:

```
@INPROCEEDINGS{bib:Domahidi2013ecos,
author={Domahidi, A. and Chu, E. and Boyd, S.},
booktitle={European Control Conference (ECC)},
title={{ECOS}: {A}n {SOCP} solver for embedded systems},
year={2013},
pages={3071-3076}
}
```
