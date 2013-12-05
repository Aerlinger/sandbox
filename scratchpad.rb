require 'active_support/all'

puts "The ARGF to this command are: #{ARGF}"
puts "The ARGV to this command are: #{ARGV}"
puts "Loadpath:"
puts $:

class Foo
  @from_class = "LOL"
  bar         = "class-level"

  puts bar

  attr_accessor :from_method
  cattr_accessor :from_method, :from_class

  def initialize
    @@from_method = "from init"
    @from_method  = "from init method"
  end

  def say_something
    puts @@class_level_attribute
  end
end

foo = Foo.new

puts Foo.from_method
puts Foo.from_class
puts foo.from_method

