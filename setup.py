from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages= find_packages(exclude=['tests*']),
    license='MIT',
    description='example my custom package',
    long_description=open('README.md').read(),
    install_requires = ['numpy'],
    url='https://github.com/Onyango-S/mypackage',
    author= 'Stephen Onyango',
    author_email='onyangosteve99@gmail.com',
   
   
)
