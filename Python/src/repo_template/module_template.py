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
Module Docstring
================

When a user runs import PythonTemplate; help(PythonTemplate), this string appears in the
DESCRIPTION section.
"""

import argparse
import logging

# Set up our logger
logger = logging.getLogger(__name__)
# Remove any previously created handlers. Otherwise, you'll get duplicate output after a reload of this module.
for handler in list(logger.handlers):
    logger.removeHandler(handler)
logger.setLevel(logging.INFO)
_console_log_handler = logging.StreamHandler()
logger.addHandler(_console_log_handler)


def func_template(arg_one, arg_two='Arg2 Default Val', *args, **kwargs):
    """
    The function docstring.
    :param arg_one: A required argument
    :param arg_two: An optional arg with a default value
    :param args: A list of any remaining positional (non-keyword) args
    :param kwargs: A dictionary of any remaining keyword args
    :return: A dictionary of all arguments.
    """
    return {
        'arg_one': arg_one,
        'arg_two': arg_two,
        'args': args,
        'kwargs': kwargs,
    }


def pyversion_str():
    """
    This function is here to show how to have Python version specific code, test it correctly, and combine coverage
    reports to get 100% code coverage with your tests.
    :return: A string representing the Python version.
    """
    import sys
    # See the Release Schedules section of https://www.python.org/downloads/
    if sys.version_info >= (3, 8):
        return "Wow, this is a really new version of Python"
    elif sys.version_info >= (3, 7):
        return "Python v3.7"
    elif sys.version_info >= (3, 6):
        return "Python v3.6"
    elif sys.version_info >= (3, 5):
        return "Python v3.5"
    elif sys.version_info >= (3, 4):
        return "Python v3.4"
    elif (2, 7) <= sys.version_info < (2, 8):
        return "Python v2.7"
    else:
        return "Unknown Version"


def main(args=None):
    # Parse our command line options
    cmd_line_parser = argparse.ArgumentParser(
        # Text to display before the argument help
        description="This text is displayed before the argument help.",
        epilog="Send any questions/concerns to CarlSapp@gmail.com."
    )
    # Our optional arguments
    cmd_line_parser.add_argument('-a', '--some-arg')
    # This example shows the default values for all of the arguments to add_argument() for an optional argument
    cmd_line_parser.add_argument('--default_vals', action='store', nargs='?', const=None, default=None, type=str,
                                 choices=None, required=False, help='', metavar='default_vals', dest='default_vals')

    # This section shows an example of using a custom check for an argument
    def custom_arg_check(arg_value):
        import re
        arg_value = arg_value.lower()
        if not re.match(r'^[+-]?[0-9]+$', arg_value):
            raise argparse.ArgumentTypeError("Invalid argument '%s' does not match required format" % arg_value)
        return arg_value
    cmd_line_parser.add_argument(
        '--custom-arg', type=custom_arg_check,
        help="This is an example of using a custom checker for a unique argument that doesn't fit "
             "into the typical int, str, etc types. The version here expects an argument like 5, "
             "+5, or -5."
    )
    
    # A required positional argument
    cmd_line_parser.add_argument(
        'Required Positional Argument',  # The user won't actually ever type this name, but it will appear in the help
                    # output as the name of this positional argument.
        #dest='mydest'
    )

    # This section is an example of using a subparser for more elaborate command line arguments.
    # For more details see the documentation at
    # https://docs.python.org/2/library/argparse.html#sub-commands
    subparsers = cmd_line_parser.add_subparsers(dest='command', help='Possible Commands:')
    # Our first command will be 'command_one'
    command_one_parser = subparsers.add_parser('command_one', help='Obtain or adjust the volume of the audio output. Executing the volume command without any arguments obtains the current volume output.')
    command_one_parser.add_argument(
        'command_one_arg',
        help='A required positional argument for the command_one command'
    )
    # Our second command will be 'command_two'
    command_two_parser = subparsers.add_parser('command_two', help='Obtain or adjust the volume of the audio output. Executing the volume command without any arguments obtains the current volume output.')
    command_two_parser.add_argument('command_two_arg', help='Volume to set.', nargs='?', default=None)

    cmd_line_args = cmd_line_parser.parse_args(args)

    if cmd_line_args.command == 'command_one':
        print("The command_one command was detected and the positional argument after the command "
              "is " + str(cmd_line_args.command_one_arg))
    elif cmd_line_args.command == 'command_two':
        print("The command_two command was detected and the positional argument after the command "
              "is " + str(cmd_line_args.command_two_arg))


if __name__ == '__main__':
    main()