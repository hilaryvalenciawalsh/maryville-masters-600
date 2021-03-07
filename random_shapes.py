import random
#screen is 500 by 500
theNewFile = input('Enter the drawing file name to create: ')
numOfShapes = int(input('Enter the number of shapes to make: '))
file = open(theNewFile,'w')
#red green blue
for integer in range(numOfShapes):
    type = random.randint(0,1)
    if type == 0:
        left = [random.randint(0,450),random.randint(0,450)]
        while left[0] == 450 and left[450] == 0:
            left = [random.randint(0,450),random.randint(0,450)]
        right = [random.randint(left[0]+1,450), random.randint(left[1]+1,450)]
        greenColor = random.randint(100,191)
        blueColor = random.randint(192,255)
        redColor = random.randint(0,99)
        
        if integer == numOfShapes-1:
            file.write('Rectangle; '+str(left[0])+', '+str(left[1])+'; '+str(right[0])+', '+str(right[1])+'; '+str(redColor)+', '+str(greenColor)+', '+str(blueColor))
        else:
            file.write('Rectangle; '+str(left[0])+', '+str(left[1])+'; '+str(right[0])+', '+str(right[1])+'; '+str(redColor)+', '+str(greenColor)+', '+str(blueColor)+'\n')
    else:
        center = [random.randint(0,450),random.randint(0,450)]
        if center[0] > center[1]:
            radiusOfCircle = random.randint(0,450-center[0])
        else:
            radiusOfCircle = random.randint(0,450-center[1])
        greenColor = random.randint(100,191)
        blueColor = random.randint(192,255)
        redColor = random.randint(0,99)
        if integer == numOfShapes-1:   
            file.write('Circle; '+str(center[0])+', '+str(center[1])+'; '+str(radiusOfCircle)+'; '+str(redColor)+', '+str(blueColor)+', '+str(greenColor))
        else:
            file.write('Circle; '+str(center[0])+', '+str(center[1])+'; '+str(radiusOfCircle)+'; '+str(redColor)+', '+str(blueColor)+', '+str(greenColor)+'\n')
file.close()
