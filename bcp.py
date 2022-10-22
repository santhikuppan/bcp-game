import random


comp_wins=0
player_wins=0
def choose_option():
    user_choice=input("choose Break,Continue or Pass: ")
    if user_choice in["Break","break","b","B"]:
        user_choice="b"
    elif user_choice in["Continue","continue","c","C"]:
         user_choice="c"
    elif user_choice in["Pass","pass","p","P"]:
         user_choice="p"
    else:
        print("I don't understand,try again.")
        choose_option()
    return user_choice  
def computer_option():
    comp_choice=random.randint(1,3) 
    if comp_choice==1:
        comp_choice="b" 
    elif comp_choice==2:
        comp_choice="c"
    else:
        comp_choice="p" 
    return comp_choice
while True:
    print("")
    user_choice=choose_option()
    comp_choice=computer_option()
    print("")
    if user_choice=="b":
        if comp_choice=="b":
            print("You chose break.The computer chose break.You tied.") 
        elif comp_choice=="c":
            print("You chose break.The computer chose continue.You lose.") 
            comp_wins+=1
        elif comp_choice=="p":
            print("You chose break.The computer chose pass.You win.")
            player_wins+=1
    elif user_choice=="c":
        if comp_choice=="b":
            print("You chose continue. The computer chose break.You win.")
            player_wins+=1
        elif comp_choice=="c":
            print("You chose continue.The computer chose continue.You tied.")   
        elif comp_choice=="p":
            print("You chose  continue. The computer chose pass.You lose.")
            comp_wins+=1
    elif user_choice=="p":
        if comp_choice=="b":
            print("You chose pass. The computer chose break.You lost.")
            comp_wins+=1
        elif comp_choice=="c":
            print("You chose pass. The computer chose continue.You win.")
            player_wins+=1 
        elif comp_choice=="p":
            print("You chose pass. The computer chose pass.You tied.")
    print("")
    print("Player wins: "+ str(player_wins))
    print("computer wins: "+ str(comp_wins))
    print("")
    user_choice=input("Do you want to play again?(y/n)")
    if user_choice in["Y","y","yes","Yes"]:
        pass
    elif user_choice in["N","n","no","No"]:
        break
    else:
        break



                       
                       
