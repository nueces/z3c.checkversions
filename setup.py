from setuptools import setup, find_packages
import os

version = '0.2dev'

setup(name='z3c.checkversions',
      version=version,
      description="Checks package versions",
      long_description=open("README.txt").read() + "\n" +
                       open("HISTORY.txt").read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
       "Programming Language :: Python",
       'Development Status :: 4 - Beta',
       'Environment :: Console',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: Zope Public License',
       'Programming Language :: Python',
       'Natural Language :: English',
       'Operating System :: OS Independent',
       'Topic :: Software Development :: Quality Assurance',
       'Framework :: Zope2',
       'Framework :: Zope3',
       'Framework :: Buildout',
        ],
      keywords='version, buildout, packages, upgrade, zope, ztk',
      author='Christophe Combelles and the Zope Community',
      author_email='zope-dev@zope.org',
      url='http://pypi.python.org/pypi/z3c.checkversions',
      license='ZPL 2.1',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['z3c'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={'buildout': ['zc.buildout']},
      tests_require=['zc.buildout'],
      test_suite='z3c.checkversions.test.test',
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      checkversions = z3c.checkversions.main:main
      """,
      )
