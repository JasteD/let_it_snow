from setuptools import setup, find_packages

setup(
    name='snowflake',
    version='0.1',
    packages=find_packages(include=['snowflake', 'let_it_snow.*'])
)

setup(
    name='requirements',
    packages=find_packages(include=['requirements.*'])
)