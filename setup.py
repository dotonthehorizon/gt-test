#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A setuptools based setup module for GTrends-Test"""

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    'click',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='GTrends-Test',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="A simple test program for Google Trends.",
    long_description=readme + '\n\n' + history,
    author="Ed McConnell",
    author_email='ed.mcconnell@gmail.com',
    url='https://github.com/dotonthehorizon/gt-test',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts':[
            'gt-test=gt_test.cli:cli',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
