#!/usr/bin/env python
# -*- coding: utf-8 -*-

# adapted from
# https://github.com/kennethreitz/setup.py/blob/master/setup.py

import os
import sys

from setuptools import find_packages
from setuptools import setup


NAME = 'podfetchdbus'
DESCRIPTION = 'D-Bus plugin for podfetch'
AUTHOR = 'Alexander Keil'
AUTHOR_EMAIL = 'akeil@akeil.de'
URL = 'https://github.com/akeil/podfetchdbus'

# leave empty to read from __version__.py
VERSION = None

# leave empty to read from requirements.txt
REQUIRES = []

#------------------------------------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))

if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as versionfile:
        VERSION = versionfile.read().split('\'')[1]

readme = open(os.path.join(here, 'README.rst')).read()

if not REQUIRES:
    with open(os.path.join(here, 'requirements.txt')) as f:
        REQUIRES = [line for line in f.readlines()]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    package_dir={'podfetchdbus': 'podfetchdbus'},
    include_package_data=True,
    install_requires=REQUIRES,
    license="BSD",
    zip_safe=True,
    entry_points={
        'podfetch.events': [
            'subscription_updated = podfetchdbus:on_subscription_updated',
            'updates_complete = podfetchdbus:on_updates_complete',
            'subscription_added = podfetchdbus:on_subscription_added',
            'subscription_removed = podfetchdbus:on_subscription_removed',
        ],
        'podfetch.service': [
            'start = podfetchdbus:start',
            'stop = podfetchdbus:stop',
        ],
    }
)
