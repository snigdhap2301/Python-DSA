weight=float(input("enter weight in kg :"))
height=float(input("enter height in meters"))
bmi=weight/(height**2)
print(round(bmi))
if bmi<18.5:
    print("Your are under-weight")
elif bmi<25:
    print("You are fit and balanced")
else:
    print("You are Over-Weight ")