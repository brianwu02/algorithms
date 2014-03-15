class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_children(self, obj):
        self.children.append(obj)


class Heap(object):

    def __init__(self):
        # initialize the heap with dummy variables
        #self.heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        #self.data = [5, 4, 9, 7, 19, 8, 17, 2, 6, 5, 21]
        self.A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        self.heap_size = len(self.A) - 1
        # this attribute does not get modified.
        self.heap_length = len(self.A) - 1
        print("unsorted list: %s") % (self.A)
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
            self.swap(i, largest)
            self.max_heapify(largest)

    def build_max_heap(self):
        """runs in linear time, produces a max-heap from an unordered input array
        Input:  A => an unsorted array
        Output: A => modified to represent a heap 
        running time: O(n) where n = len(A)
        """
        for i in range(self.heap_size / 2, -1, -1):
            self.max_heapify(i)
        print("max_heap: %s") % (self.A)

    def heap_sort(self):
        """runs in O(n lg n) sorts an array in place. """
        self.build_max_heap()
        heap_length = self.heap_length
        for i in range(heap_length, 0, -1):
            self.swap(0, i)
            self.heap_size -= 1
            self.max_heapify(0)
        print ("sorted heap %s") % (self.A)

    def swap(self, i, j):
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def max_heap_insert(self):
        pass
    
    def heap_extract_max(self):
        pass

    def heap_increase_key(self):
        pass
    
    def heap_maximum(self):
        pass

if __name__ == "__main__":
    heap = Heap()
    heap.heap_sort()
