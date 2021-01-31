theirPhrase = input("Input your phrase: ")
theirQuantity = int(input("How many times should it be repeated?: "))

for theirUnique in range(theirQuantity):
    print(str(theirUnique) + "  " + theirPhrase)