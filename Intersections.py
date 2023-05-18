class Intersection:
    def __init__(self, x, y, width, height):
        self.hitbox = (x, y, width, height)
        self.center = (round((x+width)/2), round((y+height)/2))

I1 = Intersection(157, 223, 94, 94)
I2 = Intersection(415, 223, 94,94)
I3 = Intersection(689, 223, 94,94)
Intersections = [I1, I2, I3]