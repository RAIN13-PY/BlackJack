file = open('Coins.txt', 'r')
fileToWrite = open('Coins.txt', 'a')

for line in file:
    Chips = line.strip()
print("Your balance is ", Chips)

Guess = input("Would you like to buy more chips? (Y/N) ")
while Guess != "Y":
    Guess = input("Would you like to buy more chips? (Y/N) ")
if(Guess == "Y"):
    HowManyChips = float(input("How many chips would you like to buy "))
NewBalace = int(Chips) + int(HowManyChips)

fileToWrite.truncate(0)
fileToWrite.write(str(NewBalace))
print("New total ", NewBalace, "Chips")
input("press enter to leave")