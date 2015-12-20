"""docker-compose-search
command line utility to search docker-compose projects
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='docker-compose-search',

    version='1.0.1',

    description='search docker-compose projects',
    long_description=long_description,

    url='https://github.com/francescou/docker-compose-search',

    author='Francesco Uliana',
    author_email='francesco@uliana.it',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='docker compose search',

    install_requires=['requests', 'gitpython', 'termcolor'],

    scripts=['docker-compose-search']
)
