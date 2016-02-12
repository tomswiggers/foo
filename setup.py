#!/usr/bin/env python2

"""Setup module."""
from setuptools import setup, find_packages
import os


def read(fname):
    """Read and return the contents of a file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='foo',
    version='0.0.1',
    description='foo prints bar',
    long_description=read('README.md'),
    author='Tom Swiggers',
    author_email='tom.swiggers@inuits.eu',
    url='https://github.com/tomswiggers/foo',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'foo = foo:main',
        ]
    },
    dependency_links=[
    ]
)
