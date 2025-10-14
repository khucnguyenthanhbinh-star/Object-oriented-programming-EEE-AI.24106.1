from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return math.pi * self._radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self._radius

class Rectangle(Shape):
    def __init__(self, height, width):
        self._height = height
        self._width = width

    def calculate_area(self):
        return self._height * self._width

    def calculate_perimeter(self):
        return 2 * (self._height + self._width)