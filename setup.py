#!/usr/bin/env python

from distutils.core import setup

setup(name='gloom_pwn',
      version='0.1.0',
      description='Custom pwn tools',
      packages=['gloom_pwn'],
      scripts=['scripts/analyse_binary']
     )
