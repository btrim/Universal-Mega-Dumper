# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='umd',
    version='0.1.0',
    description='Universal cartridge dumper and rom toolset',
    author='René Richard',
    url='https://github.com/db-electronics/Universal-Mega-Dumper',
    license='GPLv3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'umd = umd.umd:main'
        ],
        'gui_scripts': [
            'umd-bob = umd.gui:run'
        ]
    }
    
)
