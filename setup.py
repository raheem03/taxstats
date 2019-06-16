from setuptools import setup

long_description = open('README.rst').read()

setup(name='taxstats',
      version='0.1',
      description="Python package for downloading IRS SOI data, with utilities for parsing the dictionary",
      url='http://github.com/rchaudhry/taxstats',
      author='Raheem Chaudhry',
      author_email='rchaudhry03@gmail.com',
      license='MIT',
      long_description=long_description,
      packages=['taxstats'],
      include_package_data = True,
      zip_safe=False)