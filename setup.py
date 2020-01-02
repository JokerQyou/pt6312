# coding: utf-8
import setuptools

with open('README.md', 'r') as rf:
    long_description = rf.read()

setuptools.setup(
    name='pt6312',
    version='0.1.1',
    author='Joker Qyou',
    description='Pure Python driver for PT6312-based VFD displays.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JokerQyou/pt6312',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: System :: Hardware',
    ],
    install_requires=[
        'gpiozero>=1.5.1',
    ],
)
