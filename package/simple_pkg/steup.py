#!/usr/bin/python
# -*- coding: utf-8 -*-
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# ferch values from package.xml
setup_args = generate_distutils_setup(
    packages=[''],
    package_dir={'': 'scripts'}
)

setup(**setup_args)