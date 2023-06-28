class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, item):
        self.data.append(item)
    
    def dequeue(self):
        ret_val = self.data[0]
        del self.data[0]
        return ret_val

if __name__ == '__main__':
    s = Queue()
    s.enqueue(1)
    s.enqueue(50)
    print(s.dequeue())
    s.enqueue(100)
    print(s.dequeue())
    print(s.dequeue())