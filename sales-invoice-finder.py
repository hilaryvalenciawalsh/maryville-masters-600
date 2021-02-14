with open('sales_data.csv', 'r') as csv:
    theFile = csv.read()
    theFile = theFile.split('\n')

if '' in theFile:
    theFile.remove('')

idLname = input('Search by invoice id (id) or customer last name (lname)?: ')

while idLname not in ['id', 'lname']:
    print("***ERROR: You must enter either 'id' for invoice or 'lname' for customer last name search!*** ")
    idLname = input('Search by invoice id (id) or customer last name (lname)?: ')

theSearch = input("Enter your search term: ")
output = 0

if idLname == 'id':
    for theData in theFile:
        if theData.split(',')[0] == theSearch:
            output += 1
            print(theData)
    print("{} records were found.".format(output))

else:
    for theData in theFile:
        if theData.split(',')[2] == theSearch:
            output += 1
            print(theData)
    print("{} records were found.".format(output))