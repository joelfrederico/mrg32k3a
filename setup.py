#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    README_FILE = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY_FILE = history_file.read()

REQUIREMENTS = ["pybind11"]
SETUP_REQUIREMENTS = []
TEST_REQUIREMENTS = []

setup(
    author="Joel T. Frederico, PhD",
    author_email='joelfrederico@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python package witth buffered C++ implementation of mrg32k3a",
    install_requires=REQUIREMENTS,
    license="MIT license",
    long_description=README_FILE + '\n\n' + HISTORY_FILE,
    include_package_data=True,
    keywords='mrg32k3a',
    name='mrg32k3a',
    packages=find_packages(include=['mrg32k3a']),
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
    url='https://github.com/joelfrederico/mrg32k3a',
    version='0.1.0',
    zip_safe=False,
)
