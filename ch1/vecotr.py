class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self,):
        return f"Vector(x={self.x}, y={self.y})"

    def __abs__(self,):
        from math import hypot
        return hypot(self.x, self.y)

    def __bool__(self,):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __mul__(self, other):
        return Vector(self.x*other, self.y*other)

vec = Vector(3,4)
print(vec)
print(abs(vec))
print(bool(vec))

vec2 = Vector(4,5)
print(vec+vec2)

print(vec*3)
print(bool(Vector(0,0)))
