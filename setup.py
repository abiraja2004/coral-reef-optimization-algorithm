#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import os

# python setup.py sdist
# python setup.py bdist_wheel --universal
# cd C:\Users\victor\Anaconda3\Scripts
# twine upload C:/Users/victor/Documents/Repositorios/coral-reef-optimization-algorithm/dist/*
# pip install cro --upgrade --no-cache-dir

with open('README.txt') as file:
    long_description = file.read()
    
def get_version():
    " Get version from cro.__init__ "
    path = os.path.join(os.path.dirname(__file__), 'cro/__init__.py')
    return open(path).readlines()[-1].split()[-1].strip("\"'")   

_version = get_version()	

setup(
    name='cro',
    version=_version,
    author='CRO Team',
    author_email='cro_developers@googlegroups.com',
    packages= ['cro', 'examples'],
    url='https://github.com/VictorPelaez/coral-reef-optimization-algorithm',
    license = 'MIT',
    description='Coral Reef Optimization (CRO) Algorithm',
    long_description= long_description,
    keywords ='optimization algorithm meta-heuristic coral reef',
    classifiers = [],

)

