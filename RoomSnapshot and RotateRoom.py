import math
import matplotlib.pyplot as plt
import csv


class RadialPoint:
    def __init__(self, dist, angle):
        self.dist = dist
        self.angle = angle

    def getAsXY(self):
        dist = self.dist
        angle = self.angle
        if dist < 0:
            dist = -dist
            angle = 180 + angle
            x = dist * math.sin(math.radians(90 - angle))
            y = dist * math.sin(math.radians(angle))
        elif dist > 0:
            x = dist * math.sin(math.radians(90 - angle))
            y = dist * math.sin(math.radians(angle))
        elif dist == 0:
            x = 0
            y = 0
        return x, y

class RoomSnapshot:
    def __init__(self, csvfile):
        self.radialPoints = []
        with open(csvfile, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                dist = float(row[0])
                angle = float(row[1])
                v = RadialPoint(angle, dist)
                self.radialPoints.append(v)

    def getXpoints(self):
        xpoints = []
        for i in range(len(self.radialPoints)):
            dist = self.radialPoints[i].dist
            angle = self.radialPoints[i].angle + addAngle
            if dist < 0:
                x = -dist * math.sin(math.radians(angle + 90))
            elif dist > 0:
                x = dist * math.sin(math.radians(90 - angle))
            elif dist == 0:
                x = 0
            xpoints.append(x)
        return xpoints

    def getYpoints(self):
        ypoints = []
        for i in range(len(self.radialPoints)):
            dist = self.radialPoints[i].dist
            angle = self.radialPoints[i].angle + addAngle
            if dist < 0:
                y = -dist * math.sin(math.radians(angle + 180))
            elif dist > 0:
                y = dist * math.sin(math.radians(angle))
            elif dist == 0:
                y = 0
            ypoints.append(y)
        return ypoints

    def rotateRoom(self, addAngle):
        self.angle = self.angle + addAngle


def showAsImageWithRotation(self):
    plt.scatter([x for x in room.getXpoints()], [y for y in room.getYpoints()], c='black', s=1)
    plt.show()

room = RoomSnapshot('05.csv')
addAngle = -60
showAsImageWithRotation(room)
