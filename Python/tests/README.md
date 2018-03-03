Python Unit Tests
=================

This directory contains a template Python unittest (https://docs.python.org/2/library/unittest.html) module and a
template pytest (http://www.pytest.org) unittest module. In the pytest template file, we attempt to show the features
that are unique to pytest, as pytest is capable of executing almost all of the features of Python's unittest.

For unittest modules, the test file names must begin with the word "test" for the default test discovery options. For
more details, see the unittest.TestLoader.discover function (https://docs.python.org/2/library/unittest.html#unittest.TestLoader.discover)
or test discovery documentation (https://docs.python.org/2/library/unittest.html#test-discovery). To run the unit tests,
change to this directory and run

    python -m unittest discover

Pytest will search for any file that matches test_*.py or *_test.py. For more details, see the Conventions for Python
test discovery (https://docs.pytest.org/en/latest/goodpractices.html#test-discovery). To run the pytest modules, change
to this directory and run

    pytest
