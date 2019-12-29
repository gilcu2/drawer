import numpy as np
import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
import matplotlib.cm as cm
import sys
import os
import math
import json
from circle import *
# import jsonsocket




def drawCircles(circles):
    plt.figure()
    figure = plt.gca()
    minX = sys.float_info.max
    maxX = -minX
    minY = minX
    maxY = maxX
    sqrt2 = math.sqrt(2)
    for circle in circles:
        # plot circles using the RGBA colors
        # print(label, px, py, radius)
        circleFig = plt.Circle((circle.x, circle.y), radius=circle.radius, color=circle.color, fill=False)
        figure.add_artist(circleFig)
        delta = circle.radius / sqrt2
        plt.text(circle.x + delta, circle.y + delta, circle.label, color=circle.color)
        minX = min(minX, circle.x - circle.radius)
        minY = min(minY, circle.y - circle.radius)
        maxX = max(maxX, circle.x + circle.radius)
        maxY = max(maxY, circle.y + circle.radius)
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

def json2obj(jsonString):
    dictList=json.loads(jsonString)
    r=[]
    for dict in dictList:
        r.append(dict2circle(dict))
    return r


if __name__ == '__main__':
    # circleData1 = generateCircles()
    circles=json2obj(os.getenv("DRAWER_INPUT"))
    drawCircles(circles)
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