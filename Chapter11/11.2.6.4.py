from Chapter11.Rectangle import Rectangle
from Chapter11.Point import Point

r = Rectangle(Point(0, 0), 10, 5)

print(r.contains(Point(0, 0)))
print(r.contains(Point(3, 3)))
print(not r.contains(Point(3, 7)))
print(not r.contains(Point(3, 5)))
print(r.contains(Point(3, 4.99999)))
print(not r.contains(Point(-3, -3)))