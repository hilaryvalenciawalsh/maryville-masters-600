print('This program tests if the sequence of positive numbers you input are unique!')
print('Enter -1 to quit the program :)!')

numbers = int(input('Enter the first number: '))
length = []
setting = set()

while numbers!=-1:
    length.append(numbers)
    setting.add(numbers)
    numbers = int(input('Next number: '))
if len(setting)!=len(length):
    print('The sequence',length,'is NOT unique!')
else:
    print('The sequence',length,'is unique!')