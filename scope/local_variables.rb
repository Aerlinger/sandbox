v1 = 1
puts local_variables

class MyClass # Scope gate: Entering Class
  v2 = 2
  local_variables

  def my_method # Scope gate: Entering def
    v3 = 3
    puts local_variables
  end # Scope gate: Leaving def

  puts local_variables
end # Scope gate leaving class

obj = MyClass.new
#obj.my_method
#obj.my_method

puts local_variables
