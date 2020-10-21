#!/bin/bash
set -e -x

# Compile wheels
$PYTHON -m pip install --user nose coverage
$PYTHON -m pip wheel . -w wheelhouse/

$PYTHON -m pip install --user ecos==2.0.7.post1-19-gb0a2867 --no-index --find-links=wheelhouse
$PYTHON -m nose --with-cover --cover-package=ecos src/test_interface.py src/test_interface_bb.py
