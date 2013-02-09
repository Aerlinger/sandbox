class Emulator
  def initialize(system)
    # Creates an emulator for the given system
    @system
  end

  def play(game)
    # Runs the given game in the emulator
    "Playing"
  end

  def start(game)
    # Loads the given game but doesn't run it
  end

  def screenshot
    # Returns a screenshot of the currently loaded game
    "Taking screenshot of #{@system}"
  end
end

class Game
  attr_accessor :name, :year, :system
  attr_reader :created_at

  def initialize(name, options={})
    self.name = name
    self.year = options[:year]
    self.system = options[:system]
    @created_at = Time.now
  end

  def play
    emulate do
      "Emulating"
      play(self)
    end
  end

  def screenshot
    emulate do
      "Screenshot"
      start(self)
      screenshot
    end
  end

  private

  def emulate(&block)
    begin
      emulator = Emulator.new(system)
      emulator.instance_eval(&block)
    rescue Exception => e
      puts "Emulator failed: #{e}"
    end
    emulator
  end

  alias_method :capture, :screenshot
end

game = Game.new("starcraft", {system: "SNES"})
p game.method(:screenshot)

game.play
game.screenshot

class System
  SYSTEMS = ['SNES', 'PS1', 'Genesis']
  puts "I am inside the #{self} class"

  attr_accessor :name, :year, :system

  SYSTEMS.each do |system|
    define_method "runs_on_#{system.downcase}?" do
      self.system == system
    end
  end

end


system = System.new
system.system = "SNES"
puts system.runs_on_snes?

#define_method(name) do
#  if name.match(/^runs_on_[\w|\d]+\?$/)
#    system_name = name.to_s[/_[a-z|0-9]+\?$/].gsub(/[^[a-z]|[0-9]+]/, '')
#    SYSTEMS.any? { |system| system.downcase == system_name.downcase }
#  end
#end
