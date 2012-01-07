from __future__ import print_function
from optparse import OptionParser
import os
import re
import sys

from src import euler_problems

this_dir = sys.path[0]

parser = OptionParser()
parser.add_option("-g", "--golden", dest="check", action='store_false', default=True)
(options, args) = parser.parse_args()

# refactor the if then else code to pull common subcode
# add arg to set output file
if __name__ == "__main__":
    if options.check:
        for file in os.listdir(this_dir + '/test/golden/'):
            m = re.search('problem(\d+).out', file)
            if m:
                euler_problems.main(['-p%d' %int(m.group(1))])
    else:
        for file in os.listdir(this_dir + '/src/'):
            m = re.search('^problem(\d+).py$', file)
            if m:
                euler_problems.main(['-p%d' %int(m.group(1))])

