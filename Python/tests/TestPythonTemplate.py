#!/usr/bin/env python
# -*- coding: ascii -*-
###############################################################################
# Copyright 2017 Carl Sapp
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""
Python Unittest Template
========++++++++========

This module shows the most popular pieces of the Python unittest module.
https://docs.python.org/2/library/unittest.html
"""
import sys
if sys.version_info[0] == 2:
    import StringIO
else:
    # Python 3 moved StringIO to the IO module
    from io import StringIO
import unittest
try:
    import PythonTemplate
except ImportError:
    import os
    if os.path.exists(os.path.join(os.path.abspath('..'), 'PythonTemplate.py')):
        import sys
        sys.path.append(os.path.abspath('..'))
        import PythonTemplate
    else:
        raise

class TestCmdLineInterface(unittest.TestCase):
    """
    This class attempts to test all features of the command line interface in the PythonTemplate
    module.
    """
    def setUp(self):
        """
        This special function (must be called setUp) is called before every test* function. It
        should contain any setup code that needs to be run for all tests.
        """
        print("In TestCmdLineInterface.setUp()")
        # Most of these tests check stdout, lets redirect to something we can parse
        self.old_stdout = sys.stdout
        sys.stdout = StringIO()

    def test00CommandOne(self):
        """
        We include a 00 in the name so that this test runs before any of the other tests.
        :return: 
        """
        self.old_stdout.write("In TestCmdLineInterface.test00CommandOne()\n")
        PythonTemplate.main(['required_arg_1', 'command_one', 'command_one_arg_value'])
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), 'The command_one command was detected and the positional argument after the command is command_one_arg_value\n')
    
    def testNoArgs(self):
        """
        Test that calling our script without any arguments causes that usage statement to appear.
        """
    
    def tearDown(self):
        """
        This special function (must be called tearDown) is called after every test* function. It
        should contain any teardown code that needs to be run for all tests.
        """
        self.old_stdout.write("In TestCmdLineInterface.tearDown()\n")
        sys.stdout = self.old_stdout
        

if __name__ == '__main__':
    unittest.main()