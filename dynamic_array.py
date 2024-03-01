from static_array import Static_Seq

class Dynamic_Array_Seq(Static_Seq):
    def __init__(self, r= 2):
        super().__init__()
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self) : return self.length

    def __iter__(self):
        for i in range(len(self)): yield self.A[i]
    def build(self,X):
        for a in X: self.insert_last(a)

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A ) // (self.r **2)
    

    def _resize(self,n):
        if(self.lower < n < self.upper): return
        m = self.r * max(n,1) ## max is for removing 0
        A = [None] * m
        self._copy_forward(0,len(self.length), A, 0)
        self.A = A
        self._compute_bounds()

    def _insert_last(self,x):
        self._resize(self.length +1)
        self.A[self.length] = x
        self.size +=1

    def _delete_last(self):
        if self.length == 0 :
            return ValueError("no element inside the array")
        self.length -=1
        self.A[self.length] = None
        self._resize(self.length)

    def insert_at(self,index,i):
        self._insert_last(None)
        self._copy_forward(index,self.length - index, self.A,index +1)
        self.A[index] = i

    def delete_at(self,index):
        if self.length == 0:
            return ValueError("no element inside the array")
        return_val = self.A[index]
        self._copy_forward(index+1, self.length - index - 1, self.A, index)
        self._delete_last()
        return return_val


    def insert_first(self,x) : self.insert_at(0,x)
    def delete_first(self):return self.delete_at(0)
    def insert_last(self,x): self.insert_at(self.length,x)
    def delete_last(self): return self.delete_at(self.length - 1)


if __name__ == "__main__":
    arr = Dynamic_Array_Seq()

    arr.insert_last(10)
    arr.insert_last(20)
    arr.insert_first(5) 
    print(arr.container)


    
    