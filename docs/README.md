# Project Documentation

This folder contains the documentation for this project. The documentation is written in
[reStructuredText](http://docutils.sourceforge.net/rst.html) and designed to be compiled using
[Sphinx](http://www.sphinx-doc.org) and [Read the Docs](https://readthedocs.org/).

# Building and Publishing

## Compilation Environment Setup

To compile the reStructuredText into HTML, Python, PIP, Sphinx, and the Read the Docs theme must
be installed. These steps only need to be executed once.

If Python isn't already installed on your system, install the latest stable version
from [Python.org](https://www.python.org/downloads/). If you're using an older version of Python
and don't have PIP installed, follow the directions in [PIP's documentation](https://pip.pypa.io/en/stable/installing/).

Install Sphinx by running

    pip install sphinx

Install the Read the Docs theme by running

    pip install sphinx_rtd_theme

## Building the Documentation

To build the documentation locally, first make sure you've executed the steps in Compilation
Environment Setup to configure your system correctly. Then, change to the docs directory and
execute

    make html

This will execute Sphinx using the configuration options in conf.py. The resulting HTML files will
appear in the _build/html/ directory. Open index.html in a browser to view the documentation.

## Publishing to Read the Docs

[Read the Docs](https://readthedocs.org/) makes it extremely easy to publish this documentation to
the web. This directory is already configured correctly to build on Read the Docs. To configure a
new project and add webhooks to auto-build this documentation, follow [the documentation on Read
the Docs site](http://docs.readthedocs.io/en/latest/getting_started.html#sign-up-and-connect-an-external-account).

# Contributing Documentation Changes

Contributions and changes to this project's documentation are always welcome. To begin, read the
section describing the file/folder structure and start making changes. To understand the
reStructuredText markup, view these helpful links:

* Insert links for learning reStructuredText