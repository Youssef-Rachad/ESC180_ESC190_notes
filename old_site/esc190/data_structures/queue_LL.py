import linkedlist

class LLQueue:
    def __ini__(self):
        self.data = linkedlist.LinkedList()
    
    def enqueue(self):
        self.data.append(item)
        
    def dequeue(self):
        ret_value = self.data.head.value
        self.data.head = self.data.head.next