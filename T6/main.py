import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def init(self, width, length):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length


class Triangle(Shape):
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def area(self):
        p = (self.first + self.second + self.third) / 2.0
        return math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third))