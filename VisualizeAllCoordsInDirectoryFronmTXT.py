import math
import os
import fnmatch
import matplotlib.pyplot as plt

class RadialPoint:
    def __init__(self, dist, angle):
        self.dist = dist
        self.angle = angle

    def getAsXY(self, dist, angle):
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


def showOnConsle(path):
    alltxtfiles = fnmatch.filter(os.scandir(path), "*.txt")
    for i in alltxtfiles:
        docname = open(i, "r")
        for line in docname:
            vectorArray = line.split(' ')
            dist = float(vectorArray[0])
            angle = float(vectorArray[1])
            v = RadialPoint(dist, angle)
            print('dist = {} angle = {} coords = {}'.format(dist, angle, v.getAsXY(dist, angle)))

def showAsImage(path):
    alltxtfiles = fnmatch.filter(os.scandir(path), "*.txt")
    for i in alltxtfiles:
        docname = open(i, "r")
        for line in docname:
            vectorArray = line.split(' ')
            dist = float(vectorArray[0])
            angle = float(vectorArray[1])
            v = RadialPoint(dist, angle)
            plt.scatter(v.getAsXY(dist, angle)[0], v.getAsXY(dist, angle)[1], c = 'black', s = 1)
    plt.show()

def selectHowToShowInfo(typeOfDispl):
    if typeOfDispl == "console":
            return showOnConsle(path)
    if typeOfDispl == "image":
            return showAsImage(path)


path = input("Enter directory path ")
display = input("How to display info (console, image)? ")
selectHowToShowInfo(display)