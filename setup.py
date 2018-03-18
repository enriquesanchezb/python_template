# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='practica',
    version='0.1.0',
    description='Sample package for Verificacion y Desarrollo',
    long_description=readme,
    author1='Mario Cavero',
    author2='Esther Gomez',
    author1_email='mario.cavero@u-tad.live.com',
    author2_email='esther.gomez@u-tad.live.com',
    packages=find_packages(exclude=('tests', 'docs'))
)