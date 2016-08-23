#!/usr/bin/env python

import sys

for line in sys.stdin:

    # Strip leading and trailing whitespace:
    line = line.strip()

    # split the words into an array:
    words = line.split()

    for word in words:

        # Write the results to STDOUT
        # This is the input for reducer.py
        print '%s\t%s' % (word, 1)