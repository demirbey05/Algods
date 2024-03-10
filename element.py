class Element:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return f'({self.key},{self.value})'

    def __repr__(self):
        return f'({self.key},{self.value})'