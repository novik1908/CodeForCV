from RadialPoint import RadialPoint
import matplotlib.pyplot as plt
import fnmatch
import os


def showOnConsle(path):
    alltxtfiles = fnmatch.filter(os.scandir(path), "*.txt")
    for i in alltxtfiles:
        docname = open(i, "r")
        for line in docname:
            vectorArray = line.split(' ')
            dist = float(vectorArray[0])
            angle = float(vectorArray[1])
            v = RadialPoint(dist, angle)
            print(f"dist = {dist} angle = {angle} coords = {v.getAsXY()}")

def showAsImage(path):
    alltxtfiles = fnmatch.filter(os.scandir(path), "*.txt")
    for i in alltxtfiles:
        docname = open(i, "r")
        for line in docname:
            vectorArray = line.split(' ')
            dist = float(vectorArray[0])
            angle = float(vectorArray[1])
            v = RadialPoint(dist, angle)
            plt.scatter(v.getAsXY()[0], v.getAsXY()[1], c='black', s=1)
    plt.show()

def selectHowToShowInfo(typeOfDispl):
    if typeOfDispl == "console":
            return showOnConsle(path)
    if typeOfDispl == "image":
            return showAsImage(path)


path = input("Enter directory path ")
display = input("How to display info (console, image)? ")
selectHowToShowInfo(display)
