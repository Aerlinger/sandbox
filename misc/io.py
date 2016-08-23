import sys
import re

def count_lines(file_name):
    try:
        f = open(file_name)
        try:
            count = 0
            for line in f.readlines():
                sys.stdout.write(line)
                count += 1
            return count
        finally:
            f.close()
    except IOError:
        print("Could not open file " + file_name)


print count_lines('yoda.txt')