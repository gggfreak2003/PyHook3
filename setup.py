'''PyHook3: Python wrapper for out-of-context input hooks in Windows

The PyHook3 package provides callbacks for global mouse and keyboard events in Windows. Python
applications register event handlers for user input events such as left mouse down, left mouse up,
key down, etc. and set the keyboard and/or mouse hook. The underlying C library reports information
like the time of the event, the name of the window in which the event occurred, the value of the
event, any keyboard modifiers, etc.
'''

from setuptools import setup, find_packages, Extension
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
  long_description = f.read()

setup(
    name='PyHook3',
    version='1.6.0',

    description='Python wrapper for out-of-context input hooks in Windows',
    long_description=long_description,
    url='https://github.com/gggfreak2003/PyHook3',
    author='Peter Parente, Markus Dod',
    author_email='mdod@hs-mittweida.de',
    license='MIT',

    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Monitoring',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: Microsoft :: Windows'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages = ['PyHook3'],
    package_dir = {'PyHook3' : ""},
    ext_modules = [Extension('PyHook3._cpyHook', ['cpyHook.i'], libraries=['user32'])],
    data_files=[('Lib/site-packages/PyHook3', ['LICENSE.rst', 'README.rst', 'CHANGELOG.txt'])]
)
