from __future__ import print_function
from optparse import OptionParser
import __main__

import problem1
import problem2
import problem3
import problem4
import problem5

def main(argv=None):
    parser = OptionParser()
    parser.add_option("-p", "--problem-num", dest="problems",help="problem number to run", action='append')
    (options, args) = parser.parse_args()

    for prob in options.problems:
        func_name = 'problem' + prob
        p = getattr(__main__, func_name)
        print(func_name + ': ' + str(p.main()))

if __name__ == "__main__":
    main()
