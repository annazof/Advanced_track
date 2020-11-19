from Chapter11.Rectangle import Rectangle
from Chapter11.Point import Point

r = Rectangle(Point(100, 50), 10, 5)
print(r.width == 10 and r.height == 5)
r.flip()
print(r.width == 5 and r.height == 10)
