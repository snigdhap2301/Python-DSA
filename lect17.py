height=int(input("enetr height"))
if height>=3:
    print("You can Ride")
    age=int(input("enter age "))
    if age==18:
        print(" Please pay 250 Rs at the counter ")
    elif age<18 and age >10:
        print("Pay 100 Rs at the counter ")
    else:
        print("Pay 500 Rs at the counter ")
else:
    print("Sorry you are not eligible for the Ride ")
print("Bye ,Was happy to help you !")
