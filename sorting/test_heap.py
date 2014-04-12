import unittest
import heapq
from heap import Heap
# Use Python's standard sort method to determine whether or not Heap sorts values correctly.
#
# Use heapq module to determine max_heapify works correctly.
# max_heapify() takes an input array and ensures that max_heap constraints are met.

class TestCase(unittest.TestCase):

    def setUp(self):
        """instantiate Heap object"""
        self.unsorted_array = [4, 10, 12, 1, 5, 8, 7, 9, 1, 25, 2, 3]
        pass

    def tearDown(self):
        """don't think anything needs to be removed."""
        pass
    
    def is_heap(self, A):
        """this method is tested for correctness"""
        return all(A[i] >= A[(i - 1) // 2] for i in range(1, len(A)))

    def max_heap_correctness(self, A):
        """simply invert values, returns True if max-heap property is satisfied."""
        A = map(lambda x: x * -1, A)
        return all(A[i] >= A[(i - 1) // 2] for i in range(1, len(A)))

    def test_sort_does_not_work(self):
        """makes sure that heap does not return a sorted array before
        sort is called. sounds stupid but needs to be done lol."""
        h = Heap(self.unsorted_array)
        
        h.build_max_heap()

        #h.heap_sort()

        list_1 = h.get_array() # should probably change this method name. bad name.
        list_2 = sorted(self.unsorted_array)

        self.assertNotEqual(list_1, list_2)

    def test_sort_correctness(self):
        """tests to see whether or not Heap sorts correctly by sorting
        a list using heap sort and comparing it to a sort using python's
        standard library sort."""
        # initialize heap with this array
        h = Heap(self.unsorted_array)
        # build the heap using max heapify
        h.build_max_heap()
        # sort the array using heap sort 
        h.heap_sort()
        list1 = h.get_array()
        list2 = sorted(self.unsorted_array)
        self.assertEqual(list1, list2)

    def test_heapsort_correctness_after_insertion(self):
        """tests to see if heap sort works properly after element
        insertion."""
        pass

    def test_is_heap_method_works(self):
        """we are using a is_heap method found on stackoverflow to verify
        heap correctness.
        heapq.heapify(list) module returns a heapified list. test to
        heapq.heapify(list) -> is_heap(list) returns true.
        """
        def is_heap(A):
            return all(A[i] >= A[(i - 1) // 2] for i in range(1, len(A)))

        list_1 = self.unsorted_array
        heapq.heapify(list_1)
        self.assertTrue(is_heap(list_1))

    def test_maxheap_to_minheap(self):
        """we can turn a max heap in to a min heap by inverting the values.
        e.g. max heap: [21, 12, 4, 8, 6, 1, 2, 2, 3, 4] is the same as 
        min heap: [-21, -12, -4, -8, -6, -1, -2, -2, -3, -4].

        Verify that is_heap => true for an inverted max heap.
        """
        # ensure max_heap does not satisfiy min-heap property.
        max_heap = [21, 12, 4, 8, 6, 1, 2, 2, 3, 4]
        self.assertFalse(self.is_heap(max_heap))

        # invert all the values and verify min-heap property.
        max_heap = map(lambda x: x * -1, max_heap)
        self.assertTrue(self.is_heap(max_heap))

    def test_heap_correctness_after_insertion(self):
        """checks to see whether or not heap constraints are satisified after insertion.
        Heap Property: each node should be greater than or equal to its parent
        The parent of element i in a binary heap stored in an array element
        is (i - 1) // 2.
        
        found on stackoverflow: 
        https://stackoverflow.com/questions/16414671/\
                determining-if-a-list-of-numbers-is-in-heap-order-python-3-2
        """
        # NOTE:
        # is_heap and heapq.heapify(x) BOTH implement min heaps and
        # Heap() uses max heap. we need to invert the values so that
        # our max-heap turns in to a min-heap to verify correctness.
        # the other alternative is to actually write a max-heap checker
        # or actually implement min-heap.

        def is_heap(A):
            return all(A[i] >= A[(i - 1) // 2] for i in range(1, len(A)))

        h = Heap(self.unsorted_array)
        h.build_max_heap()
        print h
        list_1 = h.get_array()

        self.assertTrue(is_heap(list_1))




if __name__ == "__main__":
    unittest.main()
