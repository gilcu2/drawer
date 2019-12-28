import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import sys
import os
import math
import json
# import jsonsocket

matplotlib.use('TkAgg')

class Circle:
    def __init__(self,x,y,radius,color,label):
        self.x=x
        self.y=y
        self.radious=radius
        self.color=color
        self.label=label

    def __str__(self):
        return 'Circle(%s,%s,%s,%s,%s)'%(self.x,self.y,self.radious,self.color,self.label)


def obj_dict(obj):
    return obj.__dict__


def drawCircles(circles):
    plt.figure()
    figure = plt.gca()
    minX = sys.float_info.max
    maxX = -minX
    minY = minX
    maxY = maxX
    sqrt2 = math.sqrt(2)
    for circleData in circles:
        # plot circles using the RGBA colors
        # print(label, px, py, radius)
        circle = plt.Circle((circleData.x, circleData.y), radius=circleData.radius, color=circleData.color, fill=False)
        figure.add_artist(circle)
        delta = circleData.radius / sqrt2
        plt.text(circleData.x + delta, circleData.y + delta, circleData.label, color=circleData.color)
        minX = min(minX, circleData.x - circleData.radius)
        minY = min(minY, circleData.y - circleData.radius)
        maxX = max(maxX, circleData.px + circleData.radius)
        maxY = max(maxY, circleData.py + circleData.radius)
    # print(minX, minY, maxX, maxY)
    plt.xlim([minX, maxX])
    plt.ylim([minY, maxY])
    figure.set_aspect(1.0)  # make aspect ratio square
    # plot the scatter plot
    # plt.scatter(x, y, s=0, cmap='jet', facecolors='none')
    plt.grid()
    # plt.colorbar()  # this works because of the scatter
    plt.show(block=True)
    # plt.pause(0.1)


def generateCircles():
    npoints = 5
    xs = np.random.randn(npoints)
    ys = np.random.randn(npoints)
    radiouses = np.random.random(npoints)
    colors = [cm.jet(float(index) / npoints) for index in range(npoints)]
    labels = range(npoints)
    circles=[]
    for i in range(npoints):
        circles.append(Circle(xs[i],ys[i],radiouses[i],colors[i],labels[i]))

    return circles


if __name__ == '__main__':
    # circleData1 = generateCircles()
    data=os.getenv("DRAWER_INPUT")
    circleData1=json.loads(data)
    drawCircles(circleData1)
    # circleData2 = generateCircles()
    # drawCircles(circleData2)
    # input("Press Enter to continue...")

    # host='localhost'
    # port=9999
    # server = jsonsocket.Server(host, port)
    # while True:
    #     server.accept()
    #     data = server.recv()
    #     print(data)
    #     circleData2 = generateCircles()
    #     drawCircles(circleData2)
    #     server.send({'status': 'ok'})