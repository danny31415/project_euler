from __future__ import print_function
from optparse import OptionParser
import __main__
import sys

import problem1
import problem2
import problem3
import problem4
import problem5

# need option to print to file instead of stdout

def main(argv=None):
    parser = OptionParser()
    parser.add_option("-p", "--problem-num", dest="problems", action='append',
                      help="problem number to run", default=[])
    (options, args) = parser.parse_args(argv)

    for prob in options.problems:
        lib_name = 'problem' + prob
        lib = globals()[lib_name]
        print(lib_name + ': ' + str(lib.main()))

if __name__ == "__main__":
    main()

