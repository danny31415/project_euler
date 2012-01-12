from __future__ import print_function
from optparse import OptionParser
import __main__
import sys

import problem1
import problem2
import problem3
import problem4
import problem5
import problem6

def main(argv=None):
    parser = OptionParser()
    parser.add_option("-p", "--problem-num", dest="problems", action='append',
                      help="problem number to run", default=[])
    parser.add_option("-f", "--file", dest="filename")
    (options, args) = parser.parse_args(argv)


    f = sys.stdout
    if options.filename:
        f = open(options.filename, 'w')

    for prob in options.problems:
        lib_name = 'problem' + prob
        lib = globals()[lib_name]
        f.write(lib_name + ': ' + str(lib.main()) + '\n')

    if options.filename:
        f.close()

if __name__ == "__main__":
    main()

