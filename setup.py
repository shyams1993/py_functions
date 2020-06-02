import io
import os
import sys
import setuptools
from setuptools import find_packages, setup, Command

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'py_functions',
  packages = ['py_functions'],
  version = '1.0',
  license='MIT',
  description = "Python library with some useful functions to check palindrome or not, anagram or not, nearest palindrome for integers.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'SHYAM SALIL',
  author_email = 'shyamsalil1993@gmail.com',
  url = 'https://github.com/shyams1993/py_functions',
  py_modules=['mypackage'],
  entry_points={'console_scripts': ['mycli=mymodule:cli'],},
  keywords = ['USEFUL'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.4',  
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6'
  ],
  python_requires='>=3.1',
)