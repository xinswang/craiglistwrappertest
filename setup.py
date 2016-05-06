#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



setup(
    name='craiglistwrappertest',
    packages=['craigslist'],
    version=1.0.0,
    description=('Simple Craigslist wrapper.'),
    long_description=readme,
    author='original Julio M Alegria',
    author_email='test@test.com',
    url='https://github.com/xinswang/craiglistwrappertest',
    install_requires=requires,
    license='MIT-Zero'
)