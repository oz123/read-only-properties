#!/usr/bin/env python

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 7):
    raise NotImplementedError(
        "Sorry, you need at least Python 2.7 or Python 3.3.")


long_description = open("README.md").read()


setup(name='read-only-property',
      version=0.1,
      description='Create class properties which can\'t be changed.',
      long_description=long_description,
      author='Oz Tiram',
      author_email='oz.tiram@gmail.com',
      url='https://github.com/oz123/read-only-properties.git',
      py_modules=['rop'],
      license='Python Software Foundation Lincese',
      platforms='any',
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Python Software Foundation License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ],
      )
