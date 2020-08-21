from RoomSnapshot import RoomSnapshot
from RadialPoint import RadialPoint
import matplotlib.pyplot as plt
import math
import csv


def showOnConsoleWithRotation(appendAngle):
    with open('05.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            dist = float(row[0]) + float(RoomSnapshot.rotateRoom(appendAngle))
            angle = float(row[1])
            v = RadialPoint(angle, dist)
            print('dist = {} angle = {} coords = {}'.format(dist, angle, v.getAsXY()))

def showAsImageWithRotation(appendAngle):
    x = []
    y = []
    with open('05.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
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