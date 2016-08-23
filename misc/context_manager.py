class FileContextManager():
    def __init__(self, file_name):
        print "created context manager for %s" % file_name
        self._file_name = file_name
        self._file = None

    def __enter__(self):
        print "\tentering sandwich for %s" % self._file_name
        self._file = open(self._file_name)
        return self._file

    def __exit__(self, cls, value, tb):
        print "exiting sandwich for %s" % self._file_name
        self._file.close()


def count_lines(file_name):

    with FileContextManager(file_name) as f:
        count = 0
        for line in f.readlines():
            count += 1
    return count

print count_lines('../yoda.txt')