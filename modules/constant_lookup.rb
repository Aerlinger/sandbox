module A
  module B; end
  module C
    puts B

    module D
      # First looks for A::C::D::B (doesn't exist) then searches for A::B

      puts "\nmodule A::C::D"
      puts Module.nesting
    end
  end
end

module A
  module B; end
end

module A::C
  #B
  puts "\nmodule A::C"
  puts Module.nesting
end

class A
  module B; end
end

class C < A
  B == A::B
end
