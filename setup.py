from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='azt',
    version='0.0.6',
    description="~azt is an intelligent hybrid progressive programming language",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://build.azat.ai/azt/',
    author='Yaakov Azat',
    author_email='yaakovazat@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='azt AzatAI development',
    python_requires='>=3.*',
    py_modules=['azt'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pyfiglet',
    ],
    entry_points='''
        [console_scripts]
        azt=azt:cli
    ''',
)
