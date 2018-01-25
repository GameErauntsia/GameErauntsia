from setuptools import setup, find_packages
from pip.req import parse_requirements
import sys, os
import uuid

version = '0.1'

def get_requirements(source):

    try:
        install_reqs = parse_requirements(source, session=uuid.uuid1())
    except TypeError:
        # Older version of pip.
        install_reqs = parse_requirements(source)
    required = [str(ir.req) for ir in install_reqs]
    return required

setup(
    name='gamerauntsia',
    version=version,
    description="Game Erauntsia web page project",
    long_description=open("README.rst").read(),
    classifiers=[],
    keywords='',
    author='Urtzi Odriozola',
    author_email='urtzi.odriozola@gmail.com',
    url='http://gamerauntsia.eus',
    license='AGPL3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements('requirements.txt'),
)
