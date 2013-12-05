def my_method(*args, &callable)
  puts callable.call(args)
end

my_proc = proc { |*args| return args }

begin
  my_method(%w(one two 1 4 three), &my_proc)
rescue LocalJumpError => lje
  puts "Jump Error: " + lje.message
end

my_lambda = lambda { |*args| return args }

my_method(%w(one three seven five), &my_lambda)


# Procs are variadic:

p = Proc.new { |a, b| "[#{a}, #{b}]" }

puts p.call(1, 2, 3)
puts p.call(1)
