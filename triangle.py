"""Triangle class module"""
import point
from math import sqrt

class Triangle:
    """Triangle class
    >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
    >>> triangle.is_triangle()
    True
    >>> triangle.perimeter()
    6.47213595499958
    >>> triangle.area()
    2.0
    """
    def __init__(self, point_1:point.Point, point_2:point.Point, point_3:point.Point):
        """
        Init function
        """
        self.x_1 = point_1.x_coord
        self.y_1 = point_1.y_coord
        self.x_2 = point_2.x_coord
        self.y_2 = point_2.y_coord
        self.x_3 = point_3.x_coord
        self.y_3 = point_3.y_coord
    def is_triangle(self):
        """check if 3 dots are triangle"""
        return (self.x_1 - self.x_2)*(self.y_1 - self.y_3) !=\
              (self.x_1 - self.x_3)*(self.y_1 - self.y_2)
    def perimeter(self)->float:
        """ Return triangle perimeter"""
        a = sqrt((self.x_1-self.x_2)**2  + (self.y_1 - self.y_2)**2)
        b = sqrt((self.x_2-self.x_3)**2  + (self.y_2 - self.y_3)**2)
        c = sqrt((self.x_3-self.x_1)**2  + (self.y_3 - self.y_1)**2)
        return a + b + c
    def area(self)->float:
        """Return area of the triangle"""
        a = sqrt((self.x_1-self.x_2)**2  + (self.y_1 - self.y_2)**2)
        b = sqrt((self.x_2-self.x_3)**2  + (self.y_2 - self.y_3)**2)
        c = sqrt((self.x_3-self.x_1)**2  + (self.y_3 - self.y_1)**2)
        p = (a+b+c)/2
        return sqrt(p*(p-a)*(p-b)*(p-c))
