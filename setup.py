from setuptools import setup, find_packages

setup(
    name='snowflage',
    version='0.1.0',
    packages=find_packages(include=['snowflake', 'let_it_snow.*'])
)