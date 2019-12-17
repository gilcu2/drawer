import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import sys
import math
import jsonsocket

matplotlib.use('TKAgg')

def drawCircles(circleData):
    plt.figure()
    figure = plt.gca()
    minX = sys.float_info.max
    maxX = -minX
    minY = minX
    maxY = maxX
    sqrt2 = math.sqrt(2)
    for px, py, radius, color, label in circleData:
        # plot circles using the RGBA colors
        # print(label, px, py, radius)
        circle = plt.Circle((px, py), radius=radius, color=color, fill=False)
        figure.add_artist(circle)
        delta = radius / sqrt2
        plt.text(px + delta, py + delta, label, color=color)
        minX = min(minX, px - radius)
        minY = min(minY, py - radius)
        maxX = max(maxX, px + radius)
        maxY = max(maxY, py + radius)
    # print(minX, minY, maxX, maxY)
    plt.xlim([minX, maxX])
    plt.ylim([minY, maxY])
    figure.set_aspect(1.0)  # make aspect ratio square
    # plot the scatter plot
    plt.scatter(x, y, s=0, cmap='jet', facecolors='none')
    plt.grid()
    # plt.colorbar()  # this works because of the scatter
    # plt.show(block=False)
    plt.pause(0.1)


def generateCircles():
    global x, y, circleData
    npoints = 5
    x = np.random.randn(npoints)
    y = np.random.randn(npoints)
    radiouses = np.random.random(npoints)
    colors = [cm.jet(float(index) / npoints) for index in range(npoints)]
    labels = range(npoints)
    return zip(x, y, radiouses, colors, labels)


if __name__ == '__main__':
    # circleData1 = generateCircles()
    # drawCircles(circleData1)
    # circleData2 = generateCircles()
    # drawCircles(circleData2)
    # input("Press Enter to continue...")

    host='localhost'
    port=9999
    server = jsonsocket.Server(host, port)
    while True:
        server.accept()
        data = server.recv()
        print(data)
        circleData2 = generateCircles()
        drawCircles(circleData2)
        server.send({'status': 'ok'})