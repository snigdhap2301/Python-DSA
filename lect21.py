print("1 : Small Pizza\n 2: Medium Pizza \n 3: Large Pizza")
size=input("enter the size of pizza\n")
bill=0
if size=="1":
    bill=100  
if size=="2":
    bill=200
if size=="3":
    bill=300
want_pepperoni=input("do you want  pepperoni")
if size=="1" and want_pepperoni=="y" or want_pepperoni=="Y":
    bill+=30
elif size=="2" or size=="3" and want_pepperoni=="y" or want_pepperoni=="Y":
    bill+=50
want_cheese=input("do you want extra cheese")
if want_cheese=="y" or want_cheese=="Y":
     bill+=20
print("total bill is ",bill)