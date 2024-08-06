import heapq # importlibrary

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

# Example usage of PriorityQueue
pq = PriorityQueue()
pq.put("A", 2)
pq.put("B", 1)
pq.put("C", 3)

while not pq.is_empty():
    print(pq.get())