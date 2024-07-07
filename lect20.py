#multiple if
height=int(input("enetr height"))
if height>=3:
    print("You can Ride")
    age=int(input("enter age "))
    if age==18:
        bill=250
        print(" Please pay 250 Rs at the counter ")
    elif age<18 and age >10:
        bill=100
        print("Pay 100 Rs at the counter ")
    else:
        bill=500  
        print("Pay 500 Rs at the counter ")
    want_photo=input("Do you want to take a photo (Y/N) ? ")
    if want_photo=="y" or want_photo=="Y":
        bill+=50
    print(f"your total bill is {bill} ")


else:
    print("Sorry you are not eligible for the Ride ")
print("Bye ,Was happy to help you !")
