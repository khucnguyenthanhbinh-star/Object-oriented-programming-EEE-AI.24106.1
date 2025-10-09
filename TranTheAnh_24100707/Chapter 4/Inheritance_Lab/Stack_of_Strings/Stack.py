class Stack:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        self.data.pop()

    def peek(self):
        return self.data[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    
    def __str__(self):
        return str(self.data)
    
s1 = Stack()
s2 = Stack()

s1.push("Anh Ok")
s2.push("Minh la Anh")

print(str(s2))