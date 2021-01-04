import random
import time
#############################
#         USER CODE         #
#############################
FCard = 0
Acards = 0
FirstCards = 0
Hit = True
NormalCards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
FaceCards = [10, 10, 10, 10]
while(FirstCards != 2):
    if(random.randint(1,3) == 2):
        CardhandlerL = random.choice(FaceCards)
        FirstCards += 1
        print(CardhandlerL)
        Acards = Acards + CardhandlerL
    else:
        NumberOfScards = 1
        CardhandlerL = random.choice(NormalCards)
        FirstCards += 1
        print(CardhandlerL)
        Acards = Acards + CardhandlerL
if(Acards == 21):
    print("BlackJack")
print("Total is", Acards)
#########################
#      ComputerCode     #           
#########################
if(random.randint(1,3) == 2):
    FComputerCards = random.choice(NormalCards)
else:
    FComputerCards = random.choice(FaceCards)
#########################
#      UserCode         #           
#########################
print("Dealer has", FComputerCards)
while Hit != False:
    HitI = input("Do you want to hit or stay (Y/N)")
    if(HitI == "Y"):
        if(random.randint(1, 3) == 2):
            Card = random.choice(FaceCards)
        else:
            Card = random.choice(FaceCards)
        Hit = True
        print(Card)
        
        Acards = Acards + Card
        if(Acards > 21):
            print("Bust")
            Hit = False
        else:
            print("New Total is", Acards)
    else:
        Hit = False
#########################
#      ComputerCode     #    
#########################
while(FComputerCards < 17):
    if(random.randint(1,3) == 2):
        CardHandler = random.choice(FaceCards)
    else:
        CardHandler = random.choice(NormalCards)
    FComputerCards = FComputerCards + CardHandler
    print("Dealer Card", CardHandler)
    print("Dealer has ", FComputerCards)
    time.sleep(1.5)
if(Acards == FComputerCards):
    print("PUSH")
if(Acards <= 21):
    if(FComputerCards != 21):
        if(Acards > FComputerCards):
            print("WIN")
else:
    print("You Lost :(")

input("Input added so py file doesnt close. close and open blackjack.py file to play again.")