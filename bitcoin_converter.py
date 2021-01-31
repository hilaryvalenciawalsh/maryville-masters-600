# reference used: https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
import datetime
now = datetime.datetime.now()
print("As of " + now.strftime("%m/%d/%Y at %H:%M") + ", bitcoin is currently trading at $2086 per bitcoin.")

bitcoinAmt = float(input("Enter the bitcoin amount: "))

total = str(bitcoinAmt * 2086)
print("This is worth " + total + "US dollars.")
    
    