class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        # return self.data.pop()
        ret_val = self.data[-1]
        del self.data[-1]
        return ret_val

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(50)
    print(s.pop())
    s.push(100)
    print(s.pop())
    print(s.pop())