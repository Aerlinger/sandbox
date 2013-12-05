require 'active_support/all'

module Splitter
  def split!(pages)
    pages.in_groups_of(2)
  end
end
