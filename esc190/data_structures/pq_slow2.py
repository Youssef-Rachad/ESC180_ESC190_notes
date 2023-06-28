class PriorityQueueSlow2:
    def __init__(self):
        self.data = []
        self.size = 0
    
    def insert(self, value):
        i = 0
        while i < self.size:
            if value > self.data[i]:
                break
            i += 1

        # i is the index before which we can insert value
        self.data.insert(i, value)
        self.size += 1
    
    def extract_min(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.data.pop() # O(1)