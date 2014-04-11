# Implement Heap sort in Ruby

class Heap
  
  def initialize(val=[4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    @a = val
  end

  def test_method
    puts @a
  end
end

h = Heap.new()

h.test_method
