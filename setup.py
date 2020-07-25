import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
  name='web',
  version='1.0',
  packages=find_packages(),
  include_package_data=True,
  classifiers=[
    'Environment :: Console',
    'Development Status :: 2 - Alpha',
    'Intended Audience :: Developers',
    'License :: Apache-2.0',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.7',
  ],
)
