import math

class RadialPoint:
    def __init__(self, dist, angle):
        self.dist = dist
        self.angle = angle

    def getAsXY(self):
        x = self.dist * math.sin(math.radians(90 - self.angle))
        y = self.dist * math.sin(math.radians(self.angle))
        return x, y

    def toRadial(self, x, y):
        angle = self.angle
        dist = math.sqrt((x ** 2) + (y ** 2))
        if x == 0:
            if y > 0:
                angle = 90
            if y < 0:
                angle = 270
            if y == 0:
                angle = 0
        elif x < 0:
            angle = 180 + math.degrees(math.atan(y / x))
        elif x > 0:
            if y >= 0:
                angle = math.degrees(math.atan(y / x))
            if y < 0:
                angle = 360 + math.degrees(math.atan(y / x))
        return dist, angle
