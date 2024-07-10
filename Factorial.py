n=int(input())
f=1
if n==0:
    print(f)
elif n>0:
    for i in range (1,n+1):
        f*=i
        print(f)
    print()
else:
    print("Invalid entry !")