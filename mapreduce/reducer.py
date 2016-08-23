#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

word_counts = {}

# STD output From mapper.py:
for line in sys.stdin:

    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        # count was not a number so ignore this line
        continue

    if word_counts.has_key(word):
        word_counts[word] += count
    else:
        word_counts[word] = count

for word in word_counts:
    print '%s\t%s' % (word, word_counts[word])