import random

comp_options = ["rock", "paper", "scissors"]
comp = comp_options[random.randint(0, 2)]

I_player = False
print(comp)
points = 0
while I_player == False:
    I_player_inp = input("\n type quit/exit/bye for finishing the game \n Type your decision \n rock \n paper \n scissors \n")
    if I_player_inp == comp:
        print("Tie!")
    elif I_player_inp == "rock":
        if comp == "paper":
            print("Computer choosed Paper! \n You loose! \n Paper covers rock!")
            points = points-10
            print("\n You lost 10 points! \n Total points : " + str(points))
        elif comp == "scissors":
            print("Computer choosed scissors! \n You win! \n rock smashes scissors!")
            points = points+10
    elif I_player_inp == "paper":
        if comp == "rock":
            print("\n computer choosed rock! \n You win! \n Paper covers rock!")
            points = points+10
        elif comp == "scissors":
            print("\n computer choosed scissors! \n You Loose! \n Scissors cuts paper")
            points = points-10
    elif I_player_inp == "scissors":
        if comp == "rock":
            print("\n computer choosed rock! \n You Loose! \n Rock smashes scissors")
            points = points-10
        elif comp == "paper":
            print("\n computer choosed paper! \n You win! \n Scissors cuts paper")
            points = points+10
    elif I_player_inp == "quit" or I_player_inp == "bye" or I_player_inp == "exit" :
        I_player = True
    else:
        print("Wrong input!!")
    comp = comp_options[random.randint(0, 2)]
    print("\n \n \n Total points : " + str(points))