from setuptools import setup, find_packages
import sys, os

version = '0.01'

setup(name='gamerauntsia',
      version=version,
      description="Tutoreus euskarazko open-source tutorialak",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Urtzi Odriozola',
      author_email='urtzi.odriozola@gmail.com',
      url='',
      license='cc-by-sa',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
