class Test(object):
  def method_one(self):
    print "Called method_one"

  def method_two():
    print "Called method_two"

Sample = Test
Sample = Sample()
Sample.method_one()
Test.method_one(Sample)
