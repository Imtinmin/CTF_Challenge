require "minitest/autorun"
require_relative "trello"

describe Trello do

  describe ".trello_hash" do
    it "computes the correct value" do
      assert_equal(680131659347, Trello::trello_hash('leepadg') )
      assert_equal(910897038977002, Trello::trello_hash('asparagus') )
      assert_equal(956446786872726, Trello::trello_hash('trellises') )
    end
  end

  describe ".trello_letters" do
    it "determines the correct string" do
      assert_equal('leepadg', Trello::trello_letters(680131659347) )
      assert_equal('asparagus', Trello::trello_letters(910897038977002) )
      assert_equal('trellises', Trello::trello_letters(956446786872726) )
    end
  end

end
