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
Package Docstring
================

When a user runs import package_template; help(package_template), this string appears in the
DESCRIPTION section.
"""
import logging

# Set up our logger
logger = logging.getLogger(__name__)
# Remove any previously created handlers. Otherwise, you'll get duplicate output after a reload of this module.
for handler in list(logger.handlers):
    logger.removeHandler(handler)
logger.setLevel(logging.INFO)
_console_log_handler = logging.StreamHandler()
logger.addHandler(_console_log_handler)