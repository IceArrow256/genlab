from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='genlab',
    version='0.1',
    description='Create a lab report',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/IceArrow256/genlab',
    author='IceArrow256',
    author_email='icearrow256@gmail.com',
    packages=['genlab'],
    install_requires=['ia256utilities', 'docxtpl', 'appdirs', 'pyqt5'],
    entry_points={
        'console_scripts': [
            'genlab=genlab.main:main',
        ],
    },
)
