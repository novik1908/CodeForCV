from RadialPoint import RadialPoint
import matplotlib.pyplot as plt
import math
import csv


def showOnConsle():
    with open('data/01.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            dist = float(row[0])
            angle = float(row[1])
            v = RadialPoint(dist, angle)
            print('dist = {} angle = {} coords = {}'.format(dist, angle, v.getAsXY()))

def showAsImage():
    x = []
    y = []
    with open('01.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            dist = float(row[0])
            angle = float(row[1])
            v = RadialPoint(angle, dist)
            x.append(v.getAsXY()[0])
            y.append(v.getAsXY()[1])
    plt.scatter(x, y, c = 'black', s = 1)
    plt.show()

def selectHowToShowInfo(typeOfDispl):
    if typeOfDispl == "console":
        return showOnConsle()
    if typeOfDispl == "image":
        return showAsImage()


display = input("How to display info (console, image)? ")
selectHowToShowInfo(display)