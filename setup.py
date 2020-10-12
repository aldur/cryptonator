#!/usr/bin/env/ python
# encoding: utf-8

"""Setuptools configuration file."""

import setuptools
from cryptonator import __version__, __name__

__author__ = 'aldur'


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name=__name__,
    version=__version__,
    description='A simple wrapper for the cryptonator exchange rate API.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/aldur/cryptonator',

    author='Adriano Di Luzio',
    author_email='adrianodl@hotmail.it',

    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    install_requires=['requests', ],

    keywords=["cryptonator", ],
    license='MIT',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
    ],

    zip_safe=False,
    include_package_data=True,
)
