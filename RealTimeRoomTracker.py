from RadialPoint import RadialPoint
from tkinter import *
import json
import time


class Location:
    def __init__(self, locx, locy, scale):
        self.locx = locx
        self.locy = locy
        self.scale = scale


currentLocation = Location(0, 0, 1)

def up(event):
    currentLocation.locy = currentLocation.locy+50
    c.move('group1', 0, +50)
def down(event):
    currentLocation.locy = currentLocation.locy-50
    c.move('group1', 0, -50)
def left(event):
    currentLocation.locx = currentLocation.locx+50
    c.move('group1', 50, 0)
def right(event):
    currentLocation.locx = currentLocation.locx-50
    c.move('group1', -50, 0)
def upscale(event):
    currentLocation.scale = currentLocation.scale*1.1
    currentLocation.locx = currentLocation.locx*1.1
    currentLocation.locy = currentLocation.locy*1.1
    c.scale('group2', 500, 500, 1.1, 1.1)
def downcsale(event):
    currentLocation.scale = currentLocation.scale*0.9
    currentLocation.locx = currentLocation.locx * 0.9
    currentLocation.locy = currentLocation.locy * 0.9
    c.scale('group2', 500, 500, 0.9, 0.9)

#UI
root = Tk()
c = Canvas(width=1000, height=1000, bg='white')
c.focus_set()
c.pack()
for x in range(-950, 2000, 100):
    c.create_line(x, -1000+currentLocation.locy, x, 2000+currentLocation.locy, fill="#000000")
for y in range(-950, 2000, 100):
    c.create_line(-1000+currentLocation.locx, y, 2000+currentLocation.locx, y, fill="#000000")
for x in range(-1000, 2000, 50):
    c.create_line(x, -1000+currentLocation.locy, x, 2000+currentLocation.locy, fill="#9E3900", tag="group2")
for y in range(-1000, 2000, 50):
    c.create_line(-1000+currentLocation.locx, y, 2000+currentLocation.locx, y, fill="#9E3900", tag="group2")
c.create_line(500+currentLocation.locx, -1000+currentLocation.locy,
              500+currentLocation.locx, 2000+currentLocation.locy,
              fill="#000000", width=3, tag="group2")
c.create_line(-1000+currentLocation.locx, 500+currentLocation.locy,
              2000+currentLocation.locx, 500+currentLocation.locy,
              fill="#000000", width=3, tag="group2")
c.bind('<Up>', up)
c.bind('<Down>', down)
c.bind('<Left>', left)
c.bind('<Right>', right)
c.bind('<plus>', upscale)
c.bind('<minus>', downcsale)

with open('data\lidar_replay_rotate_clockwise_from-to_positive_x_axis.replay', 'r', encoding='utf-8') as docname:
    for line in docname:
        data = json.loads(line)
        for item in enumerate(data):
            dist = 360 / len(data) * item[0]
            angle = item[1]
            v = RadialPoint(angle, dist)
            ovalx = ((v.getAsXY()[0])+currentLocation.locx)*currentLocation.scale+500
            ovaly = ((v.getAsXY()[1])+currentLocation.locy)*currentLocation.scale+500
            de = c.create_oval(ovalx, ovaly, ovalx, ovalx, fill="#ff0000", tag="group2")
            c.addtag_withtag("group3", de)
            time.sleep(1)
        c.update()
        c.delete("group3")
        c.addtag_all("group1")

root.mainloop()