year=int(input("enter the year : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It is a Leap year ")
        else:
            print("not a leap year")
    print("leap year!!")
else:
    print("Not a leap year")