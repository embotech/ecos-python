#!/bin/bash
set -e -x

# Compile wheels
$PYTHON -m --user pip install nose coverage
$PYTHON -m --user pip wheel . -w wheelhouse/

$PYTHON -m --user pip install ecos --no-index -f wheelhouse
$PYTHON -m --user nose --with-cover --cover-package=ecos src/test_interface.py src/test_interface_bb.py
