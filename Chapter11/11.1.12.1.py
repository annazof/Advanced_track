from Chapter11.Point import Point


def distance(pt1, pt2):
    dx = pt1.x - pt2.x
    dy = pt1.y - pt2.y
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    print(result)

p = Point(100,100)
q = Point(0,0)

distance(p,q)