"""
build()
len()
find(k)
insert(x)
delete(k)
find_min()
find_max()
find_next()
find_prev()
"""
def Set_From_Seq(seq):
    class set_from_seq:

        def __init__(self):
            self.A = seq()
        def build(self,X):self.A.build(X)
        def __len__(self):return len(self.A)
        def __iter__(self): yield from self.A

        def __repr__(self) -> str:
           return f'{self.A}' 
        
        def find(self,k):
            res = []
            for a in self.A:
                if a.key == k:
                    res.append(a)
            return res
        
        def insert(self,x):
            for i in range(len(self.A)):
                if self.A.get_at(i).key == x.key:
                    self.A.set_at(i,x)
                    return
            
            self.A.insert_last(x)

        def delete(self,k):
            for i in range(len(self.A)):
                if self.A.get_at(i).key == k:
                    return self.A.delete_at(i)
        
        def find(self, k):
            for x in self:
                if x.key == k: return x
            return None
        
        def find_min(self):
            out = None
            for x in self:
                if (out is None) or (x.key < out.key):
                    out = x
            return out
        
        def find_max(self):
            out = None
            for x in self:
                if (out is None) or (x.key > out.key):
                    out = x
            return out
        

        def find_next(self,k):
            out = None
            for x in self:
                if (x.key > k):
                    if (out is None) or (x.key < out.key):
                        out = x
            return out

        def find_prev(self,k):
            out = None
            for x in self:
                if (x.key < k):
                    if (out is None) or (x.key > out.key):
                        out = x
            return out

        def iter_ord(self):
            x =  self.find_min()
            while x :
                yield x
                self.find_next(x.key)
    return set_from_seq

