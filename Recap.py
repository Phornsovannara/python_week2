import random
cp = random.randint(0,2)
CP =int(cp)
if CP == 0:
    print(" computer rock")
elif CP == 1:
    print(" computer paper")
else:
    print(" computer scissirs")
player = input("Enter number 0 to 2 : ")
player = int(player)

if player == 0:
    print(" you rock")
elif player == 1:
    print(" you paper")
else:
    print(" you scissirs")
#**************************************#
if CP == player:
    print("*****Tie*****")
elif CP == 0:
    if player == 1:
        print("*****you win*****")
    elif player == 2:
        print("*****CP win*****")
elif CP == 1:
    if player == 0:
        print("*****CP win*****")
    elif player == 2:
        print("*****you win*****")
elif CP == 2:
    if player == 0:
        print("*****You win*****")
    elif player == 1:
        print("*****CP win*****")