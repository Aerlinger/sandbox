class Game
  def initialize(title)
    @title = title
  end

  def setData(data)
    @data = data
  end
end

module SayHello
  def printTitle
    puts "#{@title}"
  end

  def printData
    puts @data
  end
end

module Mixin
  def classSpeak
    puts "Speaking from class"
    puts "some data: #{@initData}"
  end
end

class Game
  include SayHello
  extend Mixin
end

game = Game.new("Metroid")

game.printTitle()
game.setData({released: 1995})
game.printData()

game.classSpeak()
Game.classSpeak()