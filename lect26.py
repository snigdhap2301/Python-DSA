import random
name=input("enter names of people to pay the bill")
names_list=name.split(",")
length=len(names_list)
choice=random.randint(0,length-1)
print(f"{names_list[choice]} will pay the bill ")