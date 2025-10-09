class Stack:
    def __init__(self):
        self.data =[]
    def push (self,item):
        if isinstance(item,str):
            seflf.data.append(item)
        else:
            raise TypeError("Only strings are allowed")
    def pop(self):
        return self.data.pop()if self.data else None
    def peek(self):
        return self.data[-1] if self.data else None
    def is_empty(self):
        return len(self.data)==0
    def __str__(self):
        return str(self.data)