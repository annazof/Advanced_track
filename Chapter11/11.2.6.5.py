from Chapter11.Rectangle import Rectangle
from Chapter11.Point import Point

def collide(r, p):
    if r.corner.x <= p.corner.x <= r.corner.x + r.width or p.corner.x <= r.corner.x <= p.corner.x + p.width:
        if r.corner.y <= p.corner.y <= r.corner.y + r.height or p.corner.y <= r.corner.y <= p.corner.y + p.height:
            return True
        else:
            return False
    else:
        return False


r = Rectangle(Point(100, 50), 10, 5)
p = Rectangle(Point(30, 50), 80, 5)

print(collide(r,p))