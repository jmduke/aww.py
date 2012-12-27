#!/usr/bin/env python
from setuptools import setup

setup(name='aww',
      author='Justin Duke',
      url='https://github.com/dukerson/aww.py',
      description='A CLI for adorable pictures.',
      scripts=['aww.py'],
      install_requires=['PIL'],
      entry_points={
          'console_scripts': {
              'aww = aww:main'
          }
      }
)
