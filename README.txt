Introduction
============

Find newer versions of your installed Python packages, or newer versions of
packages in a buildout file.

This package provides a console script named ``checkversions``.

Install
=======

you can install this package either in a virtualenv::

    $ virtualenv sandbox
    $ sandbox/bin/pip install z3c.checkversions
    $ sandbox/bin/checkversions --help

or in your system::

    $ sudo pip install z3c.checkversions
    $ checkversions --help

or in a buildout::

    [buildout]
    parts = checkversions
    
    [checkversions]
    recipe=zc.recipe.egg
    eggs=z3c.checkversions [buildout]

Note that buildout support is optional and must be enabled with [buildout] so
that zc.buildout is installed as well.

Usage
=====

::

    $ checkversions -h
    Usage: checkversions [-v] [-l LEVEL] [-i INDEX] [-b BLACKLIST] [buildout_file]
    
    This script will check new package versions of either your current installed
    distributions or a buildout file if provided. It can detect major or minor
    versions availability: level 0 gets the highest version (X.y.z), level 1 gets
    the highest intermediate version (x.Y.z), level 2 gets the highest minor
    version (x.y.Z).  Using level 2, you can automatically retrieve all bugfix
    versions of a buildout.  If you provide a blacklist file with bad versions,
    these versions won't be suggested.
    
    Options:
      -h, --help            show this help message and exit
      -l LEVEL, --level=LEVEL
                            Version level to check
      -i INDEX, --index=INDEX
                            Provide and alternative package index URL
      -b BLACKLIST, --blacklist=BLACKLIST
                            Provide a blacklist file with bad versions
      -v, --verbose         Verbose mode (prints old versions too)


Examples
========

For installed packages
----------------------

Example with a virtualenv::

    $ virtualenv --no-site-packages sandbox
    $ sandbox/bin/pip install z3c.checkversions
    $ sandbox/bin/checkversions -v -l 1
    # Checking your installed distributions
    pip=0.7.1 # was: 0.6.3

For a buildout
--------------

It can work either with a full buildout.cfg or with a simple versions.cfg file.

Here is a sample `versions.cfg` file::

    [versions]
    somepackage=0.5.3

You can create a new versions.cfg by retrieving the output ::

    $ checkversions -v -l 1 versions.cfg
    # Checking buildout file versions.cfg
    somepackage=0.6.2 # was: 0.5.0

If you provide a blacklist file, such as `blacklist.cfg` containing bad
versions, such as::

    somepackage=0.6.2
    somepackage=0.6.1

Then these versions won't be suggested::

    $ checkversions -v -l 1 versions.cfg
    # Checking buildout file versions.cfg
    somepackage=0.6.0 # was: 0.5.0


Run tests
=========

Uncompress the archive, then run::

    $ python setup.py test



