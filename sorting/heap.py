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
        self.data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        self.heap_size = len(self.data) - 1
        print(self.data)
        pass

    def get_parent(self, i):
        """ Input:  A => array representing a heap
                    i => an array index
            Output: index in A of the parent i. """
        return i / 2

    def left(self, i):
        """Input:  A => an array representing a heap
           Output: i => the index in A of the left child i
        """
        return 2 * i + 1

    def right(self, i):
        """Input:   A => an array representing a heap
                    i => an array index
           Output:  the index in A of the right child i
        """
        return 2 * (i + 1)

    def heap_length(self):
        """returns the number of elements in the array"""
        return len(self.data)

    def _heap_size(self):
        """returns how many elements in the heap are stored within array A.
        Only elements in A[1..self.heap_size] where 0 <= A.heap_size <= A.length
        are valid elements of the heap.
        """
        return len(self.data) - 1

    def max_heapify(self, i):
        """runs in O(lg n) time. maintains the max-heap property"""
        A = self.data
        left = self.left(i)
        right = self.right(i)
        if left <= self.heap_size and A[left] > A[i]:
            largest = left
        else:
            largest = i

        if right <= self.heap_size and A[right] > A[largest]:
            largest = right

        if largest != i:
            # swap A[i] and A[largest] then recursively call max_heapify down the node
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        """runs in linear time, produces a max-heap from an unordered input array
        Input:  A => an unsorted array
        Output: A => modified to represent a heap 
        running time: O(n) where n = len(A)
        """
        A = self.data
        for i in range(self.heap_size / 2, -1, -1):
            self.max_heapify(i)
        print self.data

    def heap_sort(self):
        """runs in O(n lg n) sorts an array in place. """
        self.build_max_heap()
        A = self.data
        for i in range(len(A)-1, 0, -1):
            print i
            A[0], A[i] = A[i], A[0]
            self.heap_size -= 1
            self.max_heapify(0)
        print self.data
            


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
