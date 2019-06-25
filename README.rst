=======
taxstats
=======

A Python package for downloading IRS SOI Tax Stats data, with utilities for
parsing the data dictionary.

Overview
========

The Internal Revenue Service's Statistics of Income (IRS SOI) division annually
publish selected tax stats, by U.S., state, or county.

This package provides functions to:
    * Download data from IRS SOI Tax Stats historical tables
    * Download documentation for historical table 2
    * Convert the documentation from .doc to .xls format
    * Take documentation and produce dictionary of labels

Installation
============

::
    
    # dev version
    pip install git+https://github.com/raheem03/taxstats

Usage
=====

Import
------

::

    from taxstats import *


Create an object with desired attributes
----------------------------------------

::

    # create an instance of the taxstats object
    irs = taxstats(year = 2016)
    irs = taxstats(year = 2016, level = 'state', state = 'md')
    irs = taxstats(year = 2016, level = 'county', state = 'va')
    irs = taxstats(year = 2016, level = 'us')

    irs = taxstats(table = 3)

Download data
-------------

Once you have created an instance of the taxstats object, you can access a 
method for downloading thefile with the relevant parameters to your current
working directory.

::

    irs.get_table()


Downloading documentation
-------------------------

Similarly, you can get any available documentation (for historical table 2)

::

    filename = irs.get_docs()

Parsing documentation and creating labels
-----------------------------------------

IRS only allows you to download the documentation as a .doc file. This package
comes with a utility function that downloads the file in .xls format and 
also returns a dataframe object with the dictionary that you can access.

::

    # Convert .doc to .xls and return as dataframe
    df = parse_docs(filename)


Use documentation to create dictionary of labels
------------------------------------------------

Finally, you can create a dictionary of labels using the parsed dictionary.

::

    labels = create_labels(filename)

License
=======
Code released under the MIT License.
