from __future__ import print_function
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-p", "--problem-num", dest="problem_num",help="write report to FILE", metavar="FILE")
(options, args) = parser.parse_args()

if __name__ == "__main__":
    print('Hello World!')
