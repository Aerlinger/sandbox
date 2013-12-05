def define_methods
  shared = 0

  # No scope crossing!
  Kernel.send :define_method, :counter do
    shared
  end

  # We have to use dynamic dispatch to call the private method `define_method` on kernel
  Kernel.send :define_method, :inc do |x|
    shared += x
  end
end

define_methods

puts counter
inc 4
puts counter
