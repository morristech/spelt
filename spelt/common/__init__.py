#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2008 Zuza Software Foundation
#
# This file is part of Spelt.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import gettext, pygtk

from spelt.__version__ import ver

from spelt.common.config     import Configuration
from spelt.common.exceptions import *

pygtk.require("2.0")
_ = gettext.gettext
x_generator = 'Spelt ' + ver

__all__ = [
    '_',
    'ver',
    'x_generator',
    'Configuration',
    'DuplicateModelError',
    'IDUsedError',
    'InvalidElementError',
    'InvalidSectionError',
    'LanguageDBFormatError',
    'LanguageDBFormatWarning',
    'UnknownIDError',
    'UnknownModelError'
]
