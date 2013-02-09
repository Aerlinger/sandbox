require 'rubygems'
require 'active_support/all'

module LibraryUtils

  extend ActiveSupport::Concern

  included do
    puts "Included!"
  end

  module ClassMethods
    def self.search(name="Default")
      puts "Search from ClassMethods: #{name}"
    end

    def name(name="Default")
      puts "Name From ClassMethods: #{name}"
    end
  end

end


class GameLibrary
  # Methods in LibraryUtils::ClassMethods become class methods of GameLibrary
  include LibraryUtils
end

game_lib = GameLibrary.new

#GameLibrary.search
GameLibrary.name

LibraryUtils::ClassMethods.search("Static Search on Library Utils")
#LibraryUtils::ClassMethods.name("Static Name on Library Utils")

