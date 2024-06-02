class PriorityQueueSlow:
    def __init__(self):
        self.data = []
        self.size = 0
    

    def insert(self, value):
        self.data.append(value)
        self.size += 1
    
    def extract_min(self):
        if self.size == 0:
            return None

        cur_min = self.data[0]
        cur_min_loc = 0
        for i in range(1, self.size):
            if self.data[i] < cur_min:
                cur_min = self.data[i]
                cur_min_loc = i

        del self.data[cur_min_loc]
        self.size -= 1
        return cur_min