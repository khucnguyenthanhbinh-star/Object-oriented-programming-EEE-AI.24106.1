class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.data.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.data[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    
    def __str__(self):
        return str(self.data)