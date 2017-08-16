# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:53:24 2016

@author: A B Sanyal

Stone throw Integration
"""

#Imports
import random
import math
import time
import matplotlib.pyplot as plt

#Create a timer
start_time = time.time()

#Define the function
def f(x):
    p = x**2
    return p

#Number of samples to be taken
throws = 5 * pow(10, 6)

#Number of points inside the area
inside = 0

#Range of x
xmin = -1
xmax = 1

#Range of y declared manually
#"""
ymin = 0
ymax = 1
#"""

netarea = abs((xmax - xmin) * (ymax - ymin))

iterationlist = []
timelist = []

i = 1
while (i <= throws):
    x = random.uniform(xmin, xmax)
    y = random.uniform(ymax, ymin)
    if (f(x) > 0 and y > 0 and y <= f(x)):
        inside += 1
    if (f(x) < 0 and y < 0 and y >= f(x)):
        inside -= 1
    if (i % pow(10,6) == 0):
        time_now = (time.time() - start_time)
        print(str(i) + " iterations done in " + str(time_now) + " seconds.")
        area = (inside / i) * netarea
        print("Current area:", str(area))
        timelist.append(time_now)
        iterationlist.append(i)
    i += 1

area = (inside / throws) * netarea

print("Area = " + str(area))

#plt.plot(iterationlist, timelist, '-')
#plt.show()