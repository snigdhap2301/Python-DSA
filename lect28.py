import random
print(f" 0 : Rock\n 1 : Paper\n 2 : Scissors")
user_choice=int(input("enetr your choice : "))
print(f"You chose to have {user_choice} ")
comp_choice=random.randint(0,2)
print(f"computer chose to have {comp_choice} ")
if user_choice==0:
    if user_choice==0 and comp_choice==0:
        print("No one Wins !!!")
    elif comp_choice==1:
        print("You Lose...")
    else:
        print("You win !!")
elif user_choice==1:
    if user_choice==1 and comp_choice==0:
        print("You Win !!!")
    elif comp_choice==1:
        print("No one wins ...")
    else:
        print("You Lose ...")
else:
    if user_choice==2 and comp_choice==0:
        print("You Lose...")
    elif comp_choice==1:
        print("You Win!!!")
    else:
        print("No one Wins ...")

