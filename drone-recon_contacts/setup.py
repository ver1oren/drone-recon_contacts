#!/usr/bin/env python2
from distutils.core import setup

setup(
    name='drone-recon_contacts',
    version='0.1.0',
    author='Vincent Faires, Jonathan Broche',
    scripts=['bin/drone-recon_contacts'],
    url='https://github.com/lair-framework/drone-recon_contacts',
    license='LICENSE',
    description='Parses and imports recon-ng module optiv/export_contacts JSON output into a lair project.',
    install_requires=[
        "pylair >= 1.0.2", 
        "requests == 2.7.0"
    ],
)
