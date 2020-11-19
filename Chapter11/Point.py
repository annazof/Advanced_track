class Point:
    """
    Pint class represents and manipulates x, y coordinates.
    """
    def __init__(self, x=0, y=0):
        """ Create a new point at the origin"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def distance_from_origin(self):
        distance = (self.x * self.x + self.y * self.y)** .5
        return distance

    def reflex_x(self):
        self.y = -(self.y)
        return "({}, {})".format(self.x, self.y)

    def slope_from_origin(self):
        slope = self.y / self.x
        return slope
    def get_line_to(self, d):
        a = (self.y - d.y) / (self.x - d.x)
        b = self.y - a * self.x
        return a,b


