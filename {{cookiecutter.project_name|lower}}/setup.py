#!/usr/bin/env python3

from setuptools import setup

# Version info -- read without importing
_locals = {}
with open('{{cookiecutter.project_name|lower}}/_version.py') as fp:
    exec(fp.read(), None, _locals)
version = _locals['__version__']

# README into long description
with open('README.rst') as f:
    readme = f.read()

setup(
    name='{{cookiecutter.project_name|lower}}',
    version=version,
    description='A Sphinx theme',
    long_description=readme,
    author='Masatoshi Tsushima',
    author_email='utisam@gmail.com',
    packages=['{{cookiecutter.project_name|lower}}'],
    include_package_data=True,
    entry_points = {
        'sphinx_themes': [
            'path = {{cookiecutter.project_name|lower}}:get_path',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
