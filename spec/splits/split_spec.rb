require 'spec_helper'

describe "Splitter" do
  include Splitter

  context "#split_me" do
    it "splits even number of pages" do
      page_1, page_2 = double, double
      splitted       = split!([page_1, page_2])
      splitted.should == [[page_1, page_2]]
    end

    it "splits odd number of pages" do
      page_1, page_2, page_3 = double, double, double
      splitted       = split!([page_1, page_2, page_3])
      splitted.should == [[page_1, page_2], [page_3, nil]]
    end
  end
end
