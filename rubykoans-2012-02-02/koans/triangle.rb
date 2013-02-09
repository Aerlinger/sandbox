# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   :equilateral  if all sides are equal
#   :isosceles    if exactly 2 sides are equal
#   :scalene      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.rb
# and
#   about_triangle_project_2.rb
#
def triangle(a, b, c)
  # WRITE THIS CODE
  [a, b, c].each do |i|
    raise TriangleError if i <= 0
  end

  sum = 0
  [a, b, c].each do
    |elm| sum+= elm
  end
  difference = sum - 2*[a, b, c].sort.last
  raise TriangleError if difference <= 0

  if [a, b, c].uniq.size == 1
    :equilateral
  elsif [a, b, c].uniq.size == 2
    :isosceles
  else
    :scalene
  end
end

# Error class used in part 2.  No need to change this code.
class TriangleError < StandardError
end
