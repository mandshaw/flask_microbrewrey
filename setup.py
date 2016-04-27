#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'flask-restless'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='flask_microbrewrey',
    version='1.0.0',
    description="Flask Restless Demo",
    long_description=readme + '\n\n' + history,
    author="Michael Shaw",
    author_email='michael.and.shaw@gmail.com',
    url='https://github.com/mandshaw/flask_microbrewrey',
    packages=[
        'flask_microbrewrey',
    ],
    package_dir={'flask_microbrewrey':
                 'flask_microbrewrey'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='flask_microbrewrey',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
