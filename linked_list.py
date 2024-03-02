class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def later_node(self,i):
        if i == 0:
            return self
        else:
            return self.next.later_node(i-1)
        
    def init_next(self,other):
        self.next = other


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
    def __len__(self):return self.length
    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def insert_first(self,x):
        node = LinkedListNode(x)
        node.init_next(self.head)
        self.head = node
        self.length += 1    

    
    def build(self,X):
        for a in reversed(X):
            self.insert_first(a)


    def get_at(self,i):
        if self.length == 0 or i < 0:
            raise ValueError("out of bounds") 
        return self.head.later_node(i).item
    
    def set_at(self,i,x):
        if self.length == 0 or i < 0 : 
            raise ValueError("out of bounds")
        node = self.head.later_node(i)
        node.item = x

    def delete_first(self):
        if self.length == 0:
            return None
        x = self.head.item
        self.head = self.head.next
        self.length -= 1
        return x
    
    def insert_at(self,i,x):
        if i==0 :
            self.insert_first(x)
            return
        
        if i >= len(self):
            raise ValueError("out of bounds")

        new_node = LinkedList(x)
        prev = self.head.later_node(i-1)
        prev_next = prev.next
        prev.next  = new_node
        new_node.init_next(prev_next)
        self.length += 1

    def delete_at(self,i):
        if i == 0:
            return self.delete_first()
        node = self.head.later_node(i-1)
        x = node.next.item
        node.next = node.next.next
        self.length -= 1
        return x
    
    def insert_last(self,x): self.insert_at(len(self),x)
    def delete_last(self): return self.delete_at(len(self) -1)


    