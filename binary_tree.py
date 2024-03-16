class BinaryNode:

    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
        self.parent = None
    
    def subtree_iter(self):
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    def subtree_first(self):
        if self.left:
            return self.left.subtree_first()
        return self
    def subtree_last(self):
        if self.right:
            return self.right.subtree_last()
        return self
    
    def successor(self):
        if self.right:
            return self.right.subtree_first()
        else:
            while(self.parent):
                if self.parent.left is self:
                    return self.parent
                else:
                    self = self.parent
        return None
    
    def predecessor(self):
        if self.left:
            return self.left.subtree_last()
        else:
            while(self.parent):
                if self.parent.right is self:
                    return self.parent
                else:
                    self.self.parent
        return None
    

    def subtree_insert_before(self, B):
        if self.left:
            self = self.left.subtree_last()
            self.right, B.parent = B,self
        else:
            self.left,B.parent = B,self
    
    def subtree_insert_after(self,B):
        if self.right:
            self = self.right.subtree_first()
            self.left, B.parent = B,self
        else:
            self.right,B.parent = B,self
    
    def subtree_delete(self):
        if self.right or self.left:
            if self.left:
                B = self.predecessor()
            else:
                B = self.successor()
            self.item, B.item = B.item,self.itemr
            return B.subtree_delete()
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
        return self


class BinaryTree:

    def __init__(self,nodeType = BinaryNode) -> None:
        self.nodeTyoe = nodeType
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __iter__(self):
        if self.root:
            for A in self.root.subtree_iter():
                yield A.item




                
