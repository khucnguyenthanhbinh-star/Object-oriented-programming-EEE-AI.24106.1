class Stack:
    def __init__(self):
        self.data = []
    def push(self, item: str):
        self.data.append(item)
    def pop(self):
        if not self.is_empty:
          return self.data.pop()        
        return None
    def peek(self):
        if not self.is_empty:
            return self.data.peek[-1]
        return None 
    def is_empty(self) -> bool:
        return len(self.data) == 0
    def __str__(self):
        return str(self.data)
        