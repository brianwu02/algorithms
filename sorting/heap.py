# TODO:
#   implement min-heapify

class Heap(object):
    """
    Real life Use cases:

    Due to lack of pointers since it is an array based data structure, operations tend
    to be faster than for a binary tree. 
    
    Heap Sort: one of the sorting algorithms due to the fact that sorting is done in-place.
    wit no quadratic worst-case scenario.
    
    Selection Algorithm: finding min, max, median or k-th largest element can be done in linear time
    often times constant, using heap data structure.

    Graph Algorithm: by using heap as internal traversal data structure, run time will below
    reduced by polynomial order. ex: prim's minimal spanning tree & Djikstra's shorest path.
    """

    def __init__(self,val=[4, 1, 3, 2, 16, 9, 10, 14, 8, 7]):
        # initialize the heap with dummy variables
        self.A = val
        self.heap_size = len(self.A) - 1
        # this attribute does not get modified.
        self.heap_length = len(self.A) - 1
        #print("unsorted list: %s") % (self.A)
        pass

    def get_parent(self, i):
        """returns the parent index i of the current node"""
        return i / 2

    def left(self, i):
        """returns the left child index i of the current node"""
        return 2 * i + 1

    def right(self, i):
        """returns the right child index i of the current node"""
        return 2 * (i + 1)

    def max_heapify(self, i):
        """runs in O(lg n) time. maintains the max-heap property. 
        compares the children of i'th node and assures that the 
        value of the parent node is larger than both child nodes.
        """
        left = self.left(i)
        right = self.right(i)
        if left <= self.heap_size and self.A[left] > self.A[i]:
            largest = left
        else:
            largest = i

        if right <= self.heap_size and self.A[right] > self.A[largest]:
            largest = right

        if largest != i:
            # swap A[i] and A[largest] then recursively call max_heapify down the node 
            self._swap(i, largest)
            self.max_heapify(largest)

    def build_max_heap(self):
        """runs in linear time, produces a max-heap from an unordered input array
        Input:  A => an unsorted array
        Output: A => modified to represent a heap 
        running time: O(n) where n = len(A)

        calls max_heapify for all nodes below children(root).
        """
        for i in range(self.heap_size / 2, -1, -1):
            self.max_heapify(i)
        #print("max_heap: %s") % (self.A)

    def heap_sort(self):
        """runs in O(n lg n) sorts an array in place. 
        swaps the last element(lowest value) in max heap with first element(highest)
        in heap and then calls max_heapify which will recursively move the highest
        value to the root.

        """
        self.build_max_heap()
        heap_length = self.heap_length
        for i in range(heap_length, 0, -1):
            self._swap(0, i)
            self.heap_size -= 1
            self.max_heapify(0)
        #print ("sorted heap %s") % (self.A)

    def _swap(self, i, j):
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def insert(self, key):
        """implements the max-heap-insert. """
        self.heap_size += 1
        self.A.append(None)  #self.A[self.heap_size] = None
        self.heap_increase_key(self.heap_size, key)
    
    def extract_max(self):
        if self.heap_size < 0:
            raise Exception("heap underflow")
        max = self.A[0]
        self.A[0] = self.A[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(0)
        return max

    def heap_increase_key(self, i, key):
        """increases value of A[i] to key. if key < A[i], raise exception.
        otherwise, assign the value of key to A[i].
        """
        #print("key: %s, self.A[i]: %s") % (key, self.A[i])
        if key < self.A[i]:
            raise Exception("new key is smaller than current key")
        self.A[i] = key
        while i > 0 and self.A[self.get_parent(i)] < self.A[i]:
            self._swap(i, self.get_parent(i))
            i = self.get_parent(i)
    
    def get_heap_maximum(self):
        return self.A[0]

    def get_array(self):
        return self.A

    def __repr__(self):
        return str(self.A)

if __name__ == "__main__":
    unsorted_array = [2,4,1,8,21,4,2,12,3,6]
    heap = Heap(unsorted_array)
    heap.build_max_heap()
    #print heap
    heap.insert(100)
    #print heap
    heap.heap_sort()
    print heap

    #heap.set_heap_increase_key(1, 20)
    #print heap 
