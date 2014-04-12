import unittest
from heap import Heap

"""
Use Python's standard sort method to test whether or not Heap sorts values correctly.
"""

class TestCase(unittest.TestCase):

    def setUp(self):
        """instantiate Heap object"""
        #self.h = Heap()
        pass

    def tearDown(self):
        """don't think anything needs to be removed."""
        pass

    def test_sort_correctness(self):
        """tests to see whether or not Heap sorts correctly by sorting
        a list using heap sort and comparing it to a sort using python's
        standard library sort."""
        unsorted_array = [4, 10, 12, 1, 5, 8, 7, 9, 1, 25, 2, 3]

        # initialize heap with this array
        self.h = Heap(unsorted_array)
        # build the heap using max heapify
        self.h.build_max_heap()
        # sort the array using heap sort 
        self.h.heap_sort()
        list1 = self.h.get_array()
        list2 = sorted(unsorted_array)
        self.assertEqual(list1, list2)


if __name__ == "__main__":
    unittest.main()
