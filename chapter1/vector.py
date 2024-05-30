import math


class Vector:

    """
    A class to represent a 2D vector.

    Attributes:
    x (int or float): The x-coordinate of the vector.
    y (int or float): The y-coordinate of the vector.

    Methods:
    __init__(self, x=0, y=0): Initializes the vector with coordinates x and y.
    __repr__(self): Returns a string representation of the vector.
    __abs__(self): Returns the magnitude of the vector.
    __bool__(self): Returns True if the vector is non-zero, False otherwise.
    __add__(self, other): Adds two vectors.
    __mul__(self, scaler): Multiplies the vector by a scalar.
    """
  
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        """
        Initializes the vector with coordinates x and y.

        >>> v = Vector(3, 4)
        >>> v.x
        3
        >>> v.y
        4
        """
    def __repr__(self):
        
        """
        Returns a string representation of the vector.

        >>> v = Vector(3, 4)
        >>> repr(v)
        'V(3,4)'
        """
        return f"V({self.x},{self.y})"
    def __abs__(self):
        
        """
        Returns the magnitude of the vector.

        >>> v = Vector(3, 4)
        >>> abs(v)
        5.0
        """
        return math.hypot(self.x, self.y)
        

    def __bool__(self):
        
        """
        Returns True if the vector is non-zero, False otherwise.

        >>> v = Vector(0, 0)
        >>> bool(v)
        False
        >>> v = Vector(1, 0)
        >>> bool(v)
        True
        """
        return bool(abs(self))
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        
        """
        Adds two vectors.

        >>> v1 = Vector(1, 2)
        >>> v2 = Vector(3, 4)
        >>> v1 + v2
        V(4,6)
        """
        return Vector(x,y)
    def __mul__(self,scaler):
        
        """
        Multiplies the vector by a scalar.

        >>> v = Vector(1, 2)
        >>> v * 3
        V(3,6)
        """
        return Vector(self.x*scaler,self.y*scaler)
