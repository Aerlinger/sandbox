def my_method(greeting)
  puts "#{greeting}, #{yield}!"
end

my_proc = proc { "Bill" }

my_method("hey!", &my_proc)

puts my_proc.call()
