
class Heap(object):

    def __init__(self):
        # initialize the heap with dummy variables
        self.heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        pass


    def max_heapify(self):
        """runs in O(lg n) time. maintains the max-heap property"""
        pass

    def build_max_heap(self):
        """runs in linear time, produces a max-heap from an unordered input array"""
        pass

    def heap_length(self):
        """returns the number of elements in the array"""
        pass

    def heap_sort(self):
        """runs in O(n lg n) sorts an array in place. """


    def max_heap_insert(self):
        pass
    
    def heap_extract_max(self):
        pass

    def heap_increase_key(self):
        pass
    
    def heap_maximum(self):
        pass

    def heap_size(self):
        """returns how many elements in the heap are stored within array A.
        Only elements in A[1..self.heap_size] where 0 <= A.heap_size <= A.length
        are valid elements of the heap.
        
        """
        pass

    def get_parent(self, i):
        return self.heap[i/2]

    def left(self, i):
        return self.heap[2*i]

    def right(self, i):
        return self.heap[2*i+1]
