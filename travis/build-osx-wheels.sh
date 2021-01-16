#!/bin/bash
set -e -x

# Compile wheels
$PYTHON -m pip install nose coverage --user
$PYTHON -m pip wheel . -w wheelhouse/

$PYTHON -m pip install ecos --no-index -f wheelhouse --user
$PYTHON -m nose --with-cover --cover-package=ecos src/test_interface.py src/test_interface_bb.py
