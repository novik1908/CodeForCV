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

def showOnConsle(self):
    with open('05.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            dist = float(row[0])
            angle = float(row[1])
            v = RadialPoint(dist, angle)
            print('dist = {} angle = {} coords = {}'.format(dist, angle, v.getAsXY()))

def showAsImage(self):
    x = []
    y = []
    with open('05.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            dist = float(row[0])
            angle = float(row[1])
            v = RadialPoint(angle, dist)
            x.append(v.getAsXY()[0])
            y.append(v.getAsXY()[1])
    plt.scatter(x, y, c = 'black', s = 1)
    plt.show()

def selectHowToShowInfo(typeOfDispl):
    if typeOfDispl == "console":
        return showOnConsle(path)
    if typeOfDispl == "image":
        return showAsImage(path)


display = input("How to display info (console, image)? ")
selectHowToShowInfo(display)