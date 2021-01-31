import math

bowlingBalls = int(input("How many bowling balls will be manufactured?: "))
diameter = float(input("What is the diameter of each ball in inches?: "))
volume = float(input("What is the core volume in inches cubed?: "))

radius = (diameter/2) **3
newVolume = math.pi * 4/3 * radius - 124

filler = str(newVolume * bowlingBalls)
print ("You need " + filler + " inches cubed of filler! :)")