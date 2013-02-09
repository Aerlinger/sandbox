def describe(description, &block)
  ExampleGroup.new(block).evaluate!
  #block.call
end

class ExampleGroup
  def initialize(block)
    @block = block
  end

  def evaluate!
    instance_eval(&@block)
  end

  def it(description, &block)
    block.call
  end
end


class Object
  def should
    if comparison_object
      # ...
    else
      DelayedAssertion.new(self)
    end
  end
end

class DelayedAssertion
  def initialize(subject)
    @subject = subject
  end

  def ==(other)
    raise AssertionError unless @subject == other
  end
end

class AssertionError < Exception

end