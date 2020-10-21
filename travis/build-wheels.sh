#!/bin/bash
set -e -x

# Install a system package required by our library
#yum install -y atlas-devel

# Compile wheels
for PYBIN in /opt/python/*/bin; do
    # Skip Python 3.9 because no numpy and scipy wheels yet
    if [! grep -q "cp39"]; then
      "${PYBIN}/pip" install nose coverage #-r /io/dev-requirements.txt
      "${PYBIN}/pip" wheel /io/ -w wheelhouse/
    fi
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/ecos-*.whl; do
   auditwheel repair "$whl" -w /io/wheelhouse/
done

# Move remaining wheels (numpy, scipy) into location
for whl in wheelhouse/numpy*.whl; do
    mv $whl /io/$whl
done

for whl in wheelhouse/scipy*.whl; do
    mv $whl /io/$whl
done


# Install packages and test
for PYBIN in /opt/python/*/bin/; do
    "${PYBIN}/pip" install ecos --no-index -f /io/wheelhouse
    (cd "$HOME"; "${PYBIN}/nosetests" --with-cover --cover-package=ecos /io/src/test_interface.py /io/src/test_interface_bb.py)
done
