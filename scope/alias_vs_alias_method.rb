module AliasMethod
  class User
    def full_name
      puts "Johhnie Walker"
    end

    def self.add_rename
      puts "  Defining alias_method :name, :full_name"
      alias_method :name, :full_name
    end
  end

  class Developer < User
    def full_name
      puts "Geeky geek"
    end

    puts "Calling Alias#add_rename"
    add_rename  # Called when the User class is scanned
  end
end

module Alias
  class User
    def full_name
      puts "Johnnie Walker"
    end

    def self.add_rename
      # With alias the method "name" is not able to pick the method "full_name
      #
      # Alias is a keyword and is lexically scoped (self is used at the time the source code is read)
      # "self" references the user class
      puts "  Defining  alias :name :full_name"
      alias :name :full_name
    end
  end

  class Developer < User
    def full_name
      # Alias is a class method self is calculated at runtime
      puts "Geeky geek"
    end

    puts "Calling AliasMethod#add_rename"
    add_rename  # Called when the user class is fist user
  end
end

# Runtime!
AliasMethod::Developer.new.name
Alias::Developer.new.name
