from set_from_seq import Set_From_Seq
from linked_list import LinkedList
import random
from element import Element
class HashTable:

    def __init__(self,r = 200):
        self.container = Set_From_Seq(LinkedList)
        self.A = []
        self.size = 0
        self.r = r
        self.p = 2**31  - 1 
        self.a = random.randint(0,self.p - 1)
        self.b = random.randint(0,self.p - 1)
        self._compute_bounds()
        self._resize(0)

    def __len__(self): return self.size

    def __iter__(self):
        for X in self.A:
            yield from X


    def _hash(self,key,m):
        return ((self.a *key + self.b) % self.p) % m
    
    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = (len(self.A) * 100 * 100) // (self.r * self.r)

    def _resize(self,n):
        if (n <= self.lower or n >= self.upper):
            f = self.r // 100
            if f % 100 : f+=1
            # doing ceil(r/100)

            m = max(n,1) * f
            A = [self.container() for _ in range(m)]
            for x in self:
                h = self._hash(x.key,m)
                A[h].insert(x)
            self.A = A
        self._compute_bounds()

    def find(self,key):
        h = self._hash(key,len(self.A))
        return self.A[h].find(key)
    
    def insert(self,x):
        self._resize(self.size + 1)
        h = self._hash(x.key,len(self.A))
        self.A[h].insert(x)
        self.size += 1

    def delete(self,key):
        assert len(self) > 0
        h = self._hash(key,len(self.A))
        value =  self.A[h].delete(key)
        self.size -= 1
        self._resize(self.size)
        return value
    

    def find_min(self):
        out = None

        for x in self:
            if (out == None) or (x.key < out.key):
                out = x

        return out

    def find_max(self):
        out = None
        for x in self:
            if (out == None) or (x.key > out.key):
                out = x

        return out

    def find_next(self,key):
        out = None
        for x in self:
            if x.key > key:
                if out == None or out.key > x.key:
                    out = x
        return out

    def find_prev(self,key):
        out = None
        for x in self:
            if x.key < key:
                if out == None or out.key < x.key:
                    out = x
        return out


    def iter_ord(self):
        out = self.find_min()
        while out:
            yield out
            out = self.find_next(out.key)



if __name__ == "__main__":

    htable = HashTable()
    arr = [Element(1,3),Element(1,2),Element(15,2),Element(3,4),Element(42,1),Element(2,4)]
    for a in arr:
        htable.insert(a)
    
    for i in htable.A:
        print(i)
    
    print(htable.find(3))
    print(htable.find(4))














                

