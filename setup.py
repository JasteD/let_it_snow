from setuptools import setup, find_packages

setup(
    name='snowflake',
    packages=find_packages(include=['snowflake', 'let_it_snow.*'])
)