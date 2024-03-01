from static_array import Static_Seq

class Dynamic_Array_Seq(Static_Seq):
    def __init__(self, r= 2):
        super().__init__()
        self.capacity = 0
        self.r = r

    