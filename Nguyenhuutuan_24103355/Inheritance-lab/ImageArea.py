class ImageArea:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def get_area(self):
        return self.height * self.width
    def __eq__(self, next):
        return self.get_area() == next.get_area()
    def __ne__(self, next):
        return self.get_area() != next.get_area()
    def __lt__(self, next):
        return self.get_area() < next.get_area()
    def __le__(self, next):
        return self.get_area() <= next.get_area()
    def __gt__(self, next):
        return self.get_area() > next.get_area()
    def __ge__(self, next):
        return self.get_area() >= next.get_area()
    
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)