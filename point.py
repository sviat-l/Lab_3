"""point class module"""
class Point:
    """point class
    >>> point= Point(0,1)
    >>> point.y_coord
    1
    >>> point.x_coord
    0
    """
    def __init__(self, x_coord, y_coord):
        """
        Init function
        """
        self.x_coord = x_coord
        self.y_coord = y_coord
