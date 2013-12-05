initialized_objects = ObjectSpace.count_objects
#initialized_nodes   = ObjectSpace.count_nodes
#object_size         = ObjectSpace.count_objects_size

puts "Core Ruby initializes a space of objects"

require_relative 'utils'

tell_me_about("The list of initialized objects", initialized_objects)

1000.times do
  Complex(100, 6)
end

tell_me_about("The list of updated objects", ObjectSpace.count_objects)

ObjectSpace.garbage_collect

recounted_objects = ObjectSpace.count_objects

tell_me_about("The list of initialized objects", recounted_objects)

require_relative 'helpers/press_any_key'
