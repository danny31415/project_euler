from __future__ import print_function
import filecmp
import os
import re
import shlex
import sys

from src import euler_problems

this_dir = sys.path[0]

def main():
    errors = 0
    golden_dir = this_dir + '/test/golden/'
    for gold_file in os.listdir(golden_dir):
        m = re.search('problem(\d+).out', gold_file)
        if m:
            num = int(m.group(1))
            temp_file = this_dir + '/test/out/' 'problem%d.out' % num
            euler_problems.main(shlex.split('-p%d -f%s' % (num, temp_file)))
            full_gold_path = golden_dir + gold_file
            if not filecmp.cmp(full_gold_path, temp_file):
                print('Broken: %s %s' %(full_gold_path, temp_file))
                errors += 1
    return errors

if __name__ == "__main__":
    main()
