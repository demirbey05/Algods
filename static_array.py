class Array_Seq:

    def __init__(self) -> None:
        self.length = 0
        self.container = []

    def __len__(self):
        return len(self.container)
    
    def __iter__(self):
        yield from self.container

    def __getitem__(self, index):   
        return self.container[index]
    
    def __setitem__(self, index, value):
        self.container[index] = value

    def build(self, A):
        self.container = [i for i in A]
        self.length = len(A)
    
    def _copy_forward(self, start_location,elems,A,move_location):

        ## Check if the start_location is out of range
        if start_location + elems > self.length:
            raise ValueError("Out of range")
        elif move_location + elems > len(A):
            raise ValueError("Out of range")

        for i in range(elems):
            A[move_location+i] = self.container[start_location+i]

    def insert_at(self,index,value):

        A = [None] * (self.length + 1)
        self._copy_forward(0,index,A,0)
        A[index] = value
        self._copy_forward(index,self.length-index,A,index+1)
        self.build(A)

    def delete_at(self,index):
        if self.length == 0 :
            raise ValueError("out of range")
        A = [None] * (self.length - 1)
        self._copy_forward(0,index,A,0)
        return_val  = self.container[index]
        self._copy_forward(index+1,self.length - index - 1,A,index)
        self.build(A)
        return return_val
    
    def insert_first(self,value): self.insert_at(0,value)
    def insert_last(self,value): self.insert_at(len(self),value)
    def delete_first(self): return self.delete_at(0)
    def delete_last(self) : return self.delete_at(len(self))
    


if __name__ == "__main__":
    arr = Array_Seq()

    arr.insert_last(10)
    arr.insert_last(20)
    arr.insert_first(5) 
    assert(arr.container == [5,10,20])


    