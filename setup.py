from setuptools import setup

setup(
    name='w',
    version='0.1.0',
    author='Itay Donanhirsh',
    author_email='itay@bazoo.org',
    packages=['w', 'w.test', 'w.nodes'],
    scripts=['bin/w', 'bin/iw'],
    url='http://pypi.python.org/pypi/w/',
    license='LICENSE.txt',
    description='HTTP server',
    long_description=open('README.txt').read(),
    install_requires=['web.py', 'argparse', 'filemagic'],
)