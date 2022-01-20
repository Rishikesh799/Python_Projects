import random

print("$$$ WELCOME___TO___RPS___GAME $$$")
Ywins = 0
Cwins = 0

def user():
    user_ch = input("Enter your choice Rock,Paper or Scissors :")
    if user_ch in ["Rock","rock","r","R"]:
        user_ch = "r"
    elif user_ch in ["Paper","paper","p","P"]:
        user_ch = "p"
    elif user_ch in ["Scissors","scissros","s","S"]:
        user_ch = "s"
    else:
        print("Please select proper choice : Try again")
        user()

    return user_ch



def com():
    com_ch=random.randint(1,3)
    if com_ch == 1:
        com_ch ="r"
    elif com_ch == 2:
        com_ch ="p"
    elif com_ch == 3:
        com_ch = "s"

    return com_ch

while True:

    usein = user()
    com_ch =com()

    if usein == "r":
        if com_ch == "r":
            print("Your and computer choice is same so match is tied")

        elif com_ch == "p":
            print("Your choice is rock and computer is paper so : You win....")
            Ywins = Ywins+1

        elif com_ch == "s":
            print("Your choice is Rock and computer is scissors so :You lose... ")
            Cwins=Cwins+1

    if usein == "p":
        if com_ch == "r":
            print("Your choice is paper and computer choice is Rock  so :You win...")
            Ywins = Ywins+1

        elif com_ch == "p":
            print("Your choice is paper and computer is paper so : Matched tied....")

        elif com_ch == "s":
            print("Your choice is paper and computer is scissors so :You lose... ")
            Cwins = Cwins + 1


    if usein == "s":
        if com_ch == "r":
            print("Your choice is scissors and computer choice is Rock  so :You lose...")
            Cwins=Cwins+1

        elif com_ch == "p":
            print("Your choice is scissors and computer is paper so : You win....")
            Ywins =Ywins+1

        elif com_ch == "s":
            print("Your choice is scisssors and computer is scissors so : Matched tied.... ")


    print("Player wins :",(Ywins))

    print("Computer wins :",(Cwins))

    us = input("Do you want play again ??? Yes / No ")
    if us in  ["yes","Yes","y","Y","YES"]:
        pass
    else:
        print("Thank you visit again......")
        break







