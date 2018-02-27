#!/usr/bin/env python3
#
# apply-filter.py -- Integrate spectrum over passband filter function.
#
# Copyright (C) 2017, 2018  Gabriel Szasz <gszasz@redhat.com>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""Integrate spectrum over passband filter function

usage: apply-filter.py [-h] [FILE]

Integrate spectrum over passband filter function

"""

import pyphot
import numpy as np
import argparse


__version__ = "0.1"

def main():
    description = "TBD"
    epilog = "TBD"
    arg_parser = argparse.ArgumentParser(description=description, epilog=epilog)
    arg_parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    arg_parser.add_argument("-f", metavar="FILTER", dest='filter', default="GROUND_JOHNSON_V")
    arg_parser.add_argument("spectra", metavar="FILE", nargs='*',
                            help="spectrum data")
    args = arg_parser.parse_args()

    lib = pyphot.get_library()
    f = lib[args.filter]

    for spectrum_file in args.spectra:
        spectrum_data = np.loadtxt(spectrum_file, unpack=True, dtype='float')

        passband_flux = f.get_flux(spectrum_data[0, :], spectrum_data[1, :])
        mag = -2.5 * np.log10(passband_flux) - f.Vega_zero_mag
        print(mag)

if __name__ == "__main__":
    # This code is executed only when apply-filter.py is being run
    # directly as a script.  Since local variables are allocated much faster
    # than global variables, it is a good practice to encapsulate whole initial
    # code into the main() function.
    main()
