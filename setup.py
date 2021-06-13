from setuptools import setup, find_packages
from os import path, environ

cur_dir = path.abspath(path.dirname(__file__))

with open(path.join(cur_dir, 'requirements.txt'), 'r') as f:
    requirements = f.read().split()

print(requirements)

setup(
    name='uspas-ml',
    version = 'v0.0.1',
    packages=find_packages(),
    package_dir={'accelerator_toy_models':'accelerator_toy_models'},
    author='X',
    author_email='X@X',
    keywords='USPAS ML',
    description='Supplemental package for USPAS ML Labs',
    install_requires=requirements,
    include_package_data=True,
    python_requires='>=3.6'
)
