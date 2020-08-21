from RadialPoints import RadialPoints

class RoomSnapshot:
    
    
    __self.radialPoints = []
    
    __xpoints = []
    __ypoints = []
   
    def __init__(self, strCsvData):
        with open('05.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in csvreader:
                dist = float(row[0])
                angle = float(row[1])
                v = RadialPoint(angle, dist)
                strCsvData.append(row)
                self.radialPoints.append(v)
    
    def getXpoints(self):
        for i in range(len(self.radialPoints)):
            dist = self.radialPoints[i].dist
            angle = self.radialPoints[i].angle
            if dist < 0:
                x = -dist * math.sin(math.radians(angle + 90))
            elif dist > 0:
                x = dist * math.sin(math.radians(90 - angle))
            elif dist == 0:
                x = 0
            __xpoints.append(x)
        return xpoints

    def getYpoints(self):
        for i in range(len(self.radialPoints)):
            dist = self.radialPoints[i].dist
            angle = self.radialPoints[i].angle
            if dist < 0:
                y = -dist * math.sin(math.radians(angle + 180))
            elif dist > 0:
                y = dist * math.sin(math.radians(angle))
            elif dist == 0:
                y = 0
            __ypoints.append(y)
        return ypoints

    def rotateRoom(appendAngle):
        return appendAngle