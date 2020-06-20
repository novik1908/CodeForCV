import os
import fnmatch
import random
import math

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


def toRadial(x, y):
    dist = math.sqrt((x**2) + (y**2))
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
    return RadialPoint(dist, angle)

def getAsXYspecial(dist, angle):
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

def moveObject(dx, dy, doc):
    docname = open(doc, "r")
    tcompfig = []
    for line in docname:
        vectorArray = line.split(' ')
        dist = float(vectorArray[0])
        angle = float(vectorArray[1])
        t = toRadial(getAsXYspecial(dist, angle)[0] + dx, getAsXYspecial(dist, angle)[1] + dy)
        tcompfig.append(t)
        with open('movedObject.txt', 'w', encoding='utf-8') as f:
            for i in range(len(tcompfig)):
                print('{} {}'.format(tcompfig[i].dist, tcompfig[i].angle), file=f)

vectorsFig = []
with open('test3.txt', 'w', encoding = 'utf-8') as f:
    for angle in range(0, 90, 1):
        angle = angle + random.uniform(-0.8, 0.8)
        dist = 25 + random.uniform(-0.8, 0.8)
        v = RadialPoint(dist, angle)
        vectorsFig.append(v)
    for i in range(len(vectorsFig)):
        print('{} {}'.format(vectorsFig[i].dist, vectorsFig[i].angle), file = f)

docname = open('test3.txt', "r")
tcompfig = []
for line in docname:
    vectorArray = line.split(' ')
    dist = float(vectorArray[0])
    angle = float(vectorArray[1])
    t = toRadial(getAsXYspecial(dist, angle)[0] - 50, getAsXYspecial(dist, angle)[1] - 50)
    tcompfig.append(t)

with open('test2.txt', 'w', encoding = 'utf-8') as f:
    for i in range(len(tcompfig)):
        print('{} {}'.format(tcompfig[i].dist, tcompfig[i].angle), file = f)


vectors = []
with open('test1.txt', 'w', encoding = 'utf-8') as f:
    for angle in range(0, 45, 1):
        angle = angle + random.uniform(-0.8, 0.8)
        dist = 50 / math.cos(math.radians(angle)) + random.uniform(-0.8, 0.8)
        v = RadialPoint(dist, angle)
        vectors.append(v)
    for angle in range(46, 90, 1):
        angle = angle + random.uniform(-0.8, 0.8)
        dist = 50 / math.sin(math.radians(angle)) + random.uniform(-0.8, 0.8)
        v = RadialPoint(dist, angle)
        vectors.append(v)
    for angle in range(91, 135, 1):
        angle = angle + random.uniform(-0.8, 0.8)
        dist = 50 / math.cos(math.radians(90 - angle)) + random.uniform(-0.8, 0.8)
        v = RadialPoint(dist, angle)
        vectors.append(v)
    for angle in range(136, 180, 1):
        angle = angle + random.uniform(-0.8, 0.8)
        dist = 50 / math.sin(math.radians(90 - angle)) + random.uniform(-0.8, 0.8)
        v = RadialPoint(dist, angle)
        vectors.append(v)
    for angle in range(181, 207, 1):
        angle = angle + random.uniform(-0.8, 0.8)
        dist = 50 / math.cos(math.radians(180 - angle)) + random.uniform(-0.8, 0.8)
        v = RadialPoint(dist, angle)
        vectors.append(v)
    for angle in range(243, 270, 1):
        angle = angle + random.uniform(-0.8, 0.8)
        dist = 50 / math.sin(math.radians(angle - 180)) + random.uniform(-0.8, 0.8)
        v = RadialPoint(dist, angle)
        vectors.append(v)
    for angle in range(271, 315, 1):
        angle = angle + random.uniform(-0.8, 0.8)
        dist = 50 / math.cos(math.radians(270 - angle)) + random.uniform(-0.8, 0.8)
        v = RadialPoint(dist, angle)
        vectors.append(v)
    for angle in range(316, 359, 1):
        angle = angle + random.uniform(-0.8, 0.8)
        dist = 50 / math.sin(math.radians(270 - angle)) + random.uniform(-0.8, 0.8)
        v = RadialPoint(dist, angle)
        vectors.append(v)
    for i in range(len(vectors)):
        print('{} {}'.format(vectors[i].dist, vectors[i].angle), file = f)



moveObject(40, -60, 'test1.txt')
