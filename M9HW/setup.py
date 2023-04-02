from setuptools import setup, find_packages

setup(
    name='booklover',
    version='1.0.0',
    url='https://github.com/booklover.git',
    author='Wilmer Maldonado',
    author_email='etc7fq@virginia.edu',
    description='for M09 homework',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)