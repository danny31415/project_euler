from __future__ import print_function
import os
import re
import shlex
import sys

from src import euler_problems

this_dir = sys.path[0]

def main():
    for file in os.listdir(this_dir + '/src/'):
        m = re.search('^problem(\d+).py$', file)
        if m:
            num = int(m.group(1))
            name = this_dir + '/out/' 'problem%d.out' % num
            euler_problems.main(shlex.split('-p%d -f%s' % (num, name)))

if __name__ == "__main__":
    main()
