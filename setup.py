from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['sklearn>=0.19.2']

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Trainer package for models evaluation'
)