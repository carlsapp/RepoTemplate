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
logger.setLevel(logging.INFO)
_console_log_handler = logging.StreamHandler()
_console_log_handler.setLevel(logging.INFO)
logger.addHandler(_console_log_handler)


def main(args=None):
    # Parse our command line options
    cmd_line_parser = argparse.ArgumentParser(
        # Text to display before the argument help
        description="This text is displayed before the argument help.",
        epilog="Send any questions/concerns to CarlSapp@gmail.com."
    )
    # Our optional arguments
    cmd_line_parser.add_argument('-a', '--some-arg')

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