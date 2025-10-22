class store_results:
    def __init__(self, func):
        self.func = func  
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        with open("results.txt", "a") as f:
            f.write(f"Function '{self.func.__name__}' was called. Result: {result}\n")
        return result
@store_results
def add(a, b):
    return a + b
@store_results
def mult(a, b):
    return a * b
print(add(2, 2))
print(mult(6, 4))
