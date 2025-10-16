class ImageArea:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def get_area(self):
        area = self.width * self.height
        return area
    def __eq__(a,b):
        return a.get_area() == b.get_area()
    def  __gt__(a,b):
        return a.get_area() > b.get_area()
    def  __ge__(a,b):
        return a.get_area() >= b.get_area()
    def  __lt__(a,b):
        return a.get_area() < b.get_area()
    def  __le__(a,b):
        return a.get_area() <= b.get_area()
    def  __ne__(a,b):
        return a.get_area() != b.get_area()
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

