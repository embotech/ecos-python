#!/bin/sh
python3 setup.py bdist_wheel
python setup.py sdist bdist_wheel
twine upload dist/* 
