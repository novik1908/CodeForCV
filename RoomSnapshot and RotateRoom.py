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
    def __init__(self, strCsvData):
        self.radialPoints = []
        with open('05.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                dist = float(row[0])
                angle = float(row[1])
                v = RadialPoint(angle, dist)
                strCsvData.append(row)
                self.radialPoints.append(v)

    def getXpoints(self):
        xpoints = []
        for i in range(len(self.radialPoints)):
            dist = self.radialPoints[i].dist
            angle = self.radialPoints[i].angle
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
            angle = self.radialPoints[i].angle
            if dist < 0:
                y = -dist * math.sin(math.radians(angle + 180))
            elif dist > 0:
                y = dist * math.sin(math.radians(angle))
            elif dist == 0:
                y = 0
            ypoints.append(y)
        return ypoints

    def rotateRoom(appendAngle):
        return appendAngle



def showOnConsoleWithRotation(appendAngle):
    with open('05.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            dist = float(row[0]) + float(RoomSnapshot.rotateRoom(appendAngle))
            angle = float(row[1])
            v = RadialPoint(angle, dist)
            print('dist = {} angle = {} coords = {}'.format(dist, angle, v.getAsXY()))

def showAsImageWithRotation(appendAngle):
    x = []
    y = []
    with open('05.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            dist = float(row[0]) + float(RoomSnapshot.rotateRoom(appendAngle))
            angle = float(row[1])
            v = RadialPoint(angle, dist)
            x.append(v.getAsXY()[0])
            y.append(v.getAsXY()[1])
    plt.scatter(x, y, c='black', s=1)
    plt.show()

def selectHowToShowInfoWithRotation(typeOfDispl):
    if typeOfDispl == "console":
        return showOnConsoleWithRotation(appendAngle)
    if typeOfDispl == "image":
        return showAsImageWithRotation(appendAngle)

appendAngle = input("Which angle append to rotate room? ")
typeOfDispl = input("How to display info (console, image)? ")
selectHowToShowInfoWithRotation(typeOfDispl)