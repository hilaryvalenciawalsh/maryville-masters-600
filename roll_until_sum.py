import random

print("This program rolls two 6-sided dice until their sum is a given sumRoll value.")
sumRoll = int(input("Enter the target sum to roll for: "))

diceOne = random.randint(1,6)
diceTwo = random.randint(1,6)

print("Roll: " + str(diceOne) + " and " + str(diceTwo) + ", sum is " + str(diceOne + diceTwo))
count = 1

while(diceOne + diceTwo != sumRoll):
   diceOne = random.randint(1,6)
   diceTwo = random.randint(1,6)    
   print("Roll: " + str(diceOne) + " and " + str(diceTwo) + ", sum is " + str(diceOne + diceTwo))
   count += 1
   
print("Got it in " + str(count) + " rolls!")