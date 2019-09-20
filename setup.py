from setuptools import setup

setup(
    name='azt',
    version='0.0.1',
    py_modules=['azt'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        azt=azt:cli
    ''',
)
