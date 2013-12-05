require 'pp'

def press_any_key
  puts "Press any key to continue..."
  gets
end

def tell_me_about(description = nil, something)
  puts description if description

  pp something

  press_any_key
end
