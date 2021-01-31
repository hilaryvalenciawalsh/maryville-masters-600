startOfDayScore = 0
days = int(input("How many days of Scores?: "))
for theDays in range (1, days + 1):
       thePrompt = "Enter the score for day " + str(theDays) + ":"
       startOfDayScore += int(input(thePrompt))
       
print ("The total score of the " + str(theDays) + " days is " + str(startOfDayScore))