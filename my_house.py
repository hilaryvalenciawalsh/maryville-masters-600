import graphics as g 
# Your drawing should include at least the following shapes:
# 
# three rectangles
# two lines
# one circle
# one text label
# 
# Your picture should not be boring black and white.
# 
# It should include at least three colors, tastefully distributed to bring your house to life.
# 
# Finally, it should have some interactive feature such that when a user clicks on your picture
# something changes (e.g. a color changes, a tree falls over, the sun rises, a door opens).
# The change only has to happen once.
win = g.GraphWin("House", 400, 400)
theRoofLineOne = g.Line (g.Point (200, 50), g.Point (100, 170))
theRoofLineTwo = g.Line (g.Point (200, 50), g.Point (300, 170))
theRoofLineOne.draw( win )
theRoofLineTwo.draw ( win )

theHouse = g.Rectangle (g.Point (100, 170), g.Point (300, 350))
theHouse.draw ( win )

theDoor = g.Rectangle (g.Point (180, 270), g.Point (220, 350))
theDoor.setFill("lightpink")
theDoor.draw ( win )

theWindow = g.Rectangle (g.Point(150, 200), g.Point (250,250))
theWindow.setFill("lightblue")
theWindow.draw( win )

theDoorKnob = g.Point (210, 310)
theDoorKnob.draw ( win )

theSun = g.Point(50, 50)
theSun.draw ( win )
radiusSun = g.Circle(theSun, 45)
radiusSun.draw ( win )
radiusSun.setFill("yellow")
radiusSun.setOutline("orange")
theSun.setFill("yellow")

myText = g.Text(theSun, "the Sun")
myText.setFill("black")
myText.draw ( win )

theGrass = g.Rectangle (g.Point (0, 350), g.Point (400, 400))
theGrass.setFill("green")
win.getMouse()
theGrass.draw ( win )



