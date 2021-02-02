inputFile = input("Enter sales file name: ")
outputFile = input("Enter name for total sales file: ")
reading = open(inputFile, "r")
writing = open(outputFile, "w")

for inputLines in reading.readlines():
    charge1, charge2 = inputLines.split()
    charge1, charge2 = float(charge1[1:]), float(charge2[1:])
    theTotal = str(charge1 + charge2)
    string = "$ {0:>5}".format(charge1) + "$ {0:>5}".format(charge2) + " $ {0:>5}\n".format(theTotal)
    writing.write(string)
    
reading.close()
writing.close()

print("Done writing your total to ", outputFile)