import unittest
from heap import Heap

"""
Use Python's standard sort method to test whether or not Heap sorts values correctly.
"""

class TestCase(unittest.TestCase):

    def setUp(self):
        """instantiate Heap object"""
        self.unsorted_array = [4, 10, 12, 1, 5, 8, 7, 9, 1, 25, 2, 3]
        pass

    def tearDown(self):
        """don't think anything needs to be removed."""
        pass

    def test_sort_does_not_work(self):
        """makes sure that heap does not return a sorted array before
        sort is called. sounds stupid but needs to be done lol."""



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


if __name__ == "__main__":
    unittest.main()
