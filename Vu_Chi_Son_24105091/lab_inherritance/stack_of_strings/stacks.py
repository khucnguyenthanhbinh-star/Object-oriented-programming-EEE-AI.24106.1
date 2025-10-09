class Stack:
    def __init__(self):
        self.data = []
    def push(self,item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]
    
    def __str__(self):
        return str(self.data)
    
s1=Stack()
s2=Stack()
s1.push("Tung cc")
s2.push("Tung rr")
print(str(s1))
