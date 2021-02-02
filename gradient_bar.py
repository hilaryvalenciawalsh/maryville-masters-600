import graphics as g

win = g.GraphWin("Gradient Bar", 400, 200)
width = 67
c = 0
x = 0

for boxes in range (7):
    boxOne = g.Rectangle (g.Point(x, 0), g.Point(x+67, 400))
    boxOne.setFill(g.color_rgb(0,c,0))
    boxOne.setWidth(0)
    c = c + 40
    x = x + 67
    boxOne.draw ( win )
    
#     allColors = color_rbg(0, 100, 0) this does not work, but is in the graphics folder... :(
#     boxOne.setFill(allColors)
    
# def color_rgb(r,g,b):
#     """r,g,b are intensities of red, green, and blue in range(256)
#     Returns color specifier string for the resulting color"""
#     return "#%02x%02x%02x" % (r,g,b)


#     boxTwo = g.Rectangle (g.Point(0, 0), g.Point(134, 400))
#     boxTwo.draw ( win )
#  
#     
#     boxThree = g.Rectangle (g.Point(0, 0), g.Point(201, 400))
#     boxThree.draw ( win )
#     
#     
#     boxFour = g.Rectangle (g.Point(0, 0), g.Point(268, 400))
#     boxFour.draw ( win )
#     
#     boxFive = g.Rectangle (g.Point(0, 0), g.Point(335, 400))
#     boxFive.draw ( win )
#     
#     boxSix = g.Rectangle (g.Point(0, 0), g.Point(400, 400))
#     boxSix.draw ( win )

# boxOne.setFill("green yellow")
# boxTwo.setFill("light green")
# boxThree.setFill("forest green")
# boxFour.setFill("green")
# boxFive.setFill("sea green")
# boxSix.setFill("dark green")



