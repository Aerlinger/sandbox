my_var = "hello"


MyClass = Class.new do
  puts "Declaring: " + my_var

  define_method :my_method do
    puts my_var
  end
end

obj = MyClass.new

obj.my_method
