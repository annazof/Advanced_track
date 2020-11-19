class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        area = self.height * self.width
        return area

    def perimeter(self):
        perimeter = 2*self.height + 2*self.width
        return perimeter

    def flip(self):
        self.height, self.width = self.width, self.height
        return self.height, self.width

    def contains(self, a):
        if self.corner.x <= a.x < self.width and self.corner.y <= a.y <self.height:
            return True
        else:
            return False
