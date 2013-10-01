puts "The ARGF to this command are: #{ARGF}"
puts "The ARGV to this command are: #{ARGV}"
puts "Loadpath: #{$:}"

class Foo
  #cattr_accessor :bar
  @@bar = "@@"
  @bar = "LOL"
  bar = "class-level"

  def initialize
    @@from_method = ""
  end

  puts "in class: #{bar}"
  puts "in class: #{@bar}"

  def say_something
    puts @bar
  end
end

foo = Foo.new
#puts foo.bar
foo.say_something
