require 'test/unit'
require './spec'

class TestDescribe < Test::Unit::TestCase
  def test_that_it_can_pass
    describe 'some thing' do
      it 'has some property do ' do
      end
    end
  end

  def test_that_it_can_fail
    assert_raise(IndexError) do
      describe 'some failing thing' do
        it 'fails' do
          raise IndexError
        end
      end
    end
  end

end

class TestAssertion < Test::Unit::TestCase
  def test_that_it_can_pass
    2.should == 2
    # some_object.should be_true
    # some_object.should have(4).things
  end

  def test_that_it_can_fail
    assert_raise(AssertionError) do
      1.should == 2
    end
  end
end