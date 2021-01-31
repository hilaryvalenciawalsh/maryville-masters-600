for tempConversions in range(3):
    inputCelcius = input("Enter the temperature in C: ")
    tempInCelsius = float(inputCelcius)
    tempInFarhenheit = 1.8 * tempInCelsius + 32
    print ("The temperature in Farhenheit is: ", tempInFarhenheit, "degrees" )