
class Heap(object):

    def __init__(self):
        # initialize the heap with dummy variables
        self.heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        pass


    def get_parent(self, i):
        return self.heap[i/2]

    def left(self, i):
        return self.heap[2*i]

    def right(self, i):
        return self.heap[2*i+1]
