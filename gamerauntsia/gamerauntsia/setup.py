from setuptools import setup, find_packages
import sys, os

version = '0.01'

setup(name='gamerauntsia',
      version=version,
      description="Game Erauntsia web page project",
      long_description=open("README.md").read(),
      classifiers=[],
      keywords='',
      author='Urtzi Odriozola',
      author_email='urtzi.odriozola@gmail.com',
      url='http://gamerauntsia.eus',
      license='AGPL3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'django_simple_forum',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
