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
        self.heap = [5, 4, 9, 7, 19, 8, 17, 2, 6, 5, 21]
        print(self.heap)
        pass

    def get_parent(self, i):
        """ Input:  A => array representing a heap
                    i => an array index
            Output: index in A of the parent i. """
        if i == 1:
            return None
        return (i/2)

    def left(self, i):
        """Input:  A => an array representing a heap
           Output: i => the index in A of the left child i
        """
        #if (2 * i ) <= self.heap_size():
        return 2 * i
        #else: return None

    def right(self, i):
        """Input:   A => an array representing a heap
                    i => an array index
           Output:  the index in A of the right child i
        """
        #if (2 * i + 1) <= self.heap_size():
        return 2 * i + 1
        #else: return None

    def heap_length(self):
        """returns the number of elements in the array"""
        return len(self.heap)

    def heap_size(self):
        """returns how many elements in the heap are stored within array A.
        Only elements in A[1..self.heap_size] where 0 <= A.heap_size <= A.length
        are valid elements of the heap.
        """
        return len(self.heap) - 1

    def max_heapify(self, i):
        A = self.heap
        """runs in O(lg n) time. maintains the max-heap property"""
        left = self.left(i)
        right = self.right(i)
        if left <= self.heap_size() and A[left] > A[i]:
            largest = left
        else:
            largest = i

        if right <= self.heap_size() and A[right] > A[largest]:
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
        A = self.heap
        heap_size = len(A)
        for i in range(len(A)/2, 1, -1):
            self.max_heapify(i)
        print self.heap

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

if __name__ == "__main__":
    heap = Heap()
    heap.build_max_heap()
