
graph = {
        'A': ['B', 'C', 'E'],
        'B': ['A', 'C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F', 'D'],
        'F': ['C']
        }

class Queue(object):
    """simple implementation of a queue"""

    def __init__(self):
        self.holder = []

    def enqueue(self, val):
        self.holder.append(val)

    def dequeue(self):
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]
        except:
            pass
        return val

    def isEmpty(self):
        result = False
        if len(self.holder) == 0:
            result = True
        return result


def BFS(graph, start, end, q):
    
    temp_path = [start]
    q.enqueue(temp_path)

    while q.isEmpty() == False:
        tmp_path = q.dequeue()
        last_node = tmp_path[len(tmp_path)-1]
        print tmp_path
        
        if last_node == end:
            print("VALID PATH: %s") % (tmp_path)
        
        for link_node in graph[last_node]:
            if link_node not in tmp_path:
                new_path = []
                new_path = tmp_path + [link_node]
                q.enqueue(new_path)


path_queue = Queue()
BFS(graph, "A", "F", path_queue)








