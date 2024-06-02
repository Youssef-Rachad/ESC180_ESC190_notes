class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get_i(self, i):
        # return the value at index i
        cur = self.head
        for j in range(i):
            cur = cur.next
        return cur.value

    def append(self, value):
        '''Add a new node with the value value to the end of the list'''
        # Create a new node
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node
    
    def insert(self, value, i):
        '''Insert a node with the value value at index i'''
        new_node = Node(value)

        if i == 0:
            new_node.next = self.head
            self.head = new_node
        
        else:
            cur = self.head
            for j in range(i-1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
        
        if new_node.next == None:
            self.tail = new_node

    def __str__(self):
        cur = self.head
        s = ""
        if(cur == None):
            return "Empty list :("
        
        while cur != None:
            print(cur)
            s += str(cur) + " -> "
            cur = cur.next
        return s[:-4] # remove last arrow

if __name__ == '__main__':
    LL = LinkedList()
    LL.append(3)
    LL.append(50)
    LL.append(100)

    print(LL)