from setuptools import setup

setup(
    name='snl',
    version='0.1',
    description='Sequential neural likelihood',
    url='https://github.com/gpapamak/snl',
    author='Marcel Nonnenmacher (original code from George Papamakarios)',
    packages=['snl', 'snl.ml', 'snl.ml.models', 'snl.pdfs', 'snl.simulators', 'snl.util', 
              'snl.inference', 'snl.inference.diagnostics'],
    license='MIT',
    install_requires=['numpy', 'scipy', 'theano'],
    dependency_links=[]
)
