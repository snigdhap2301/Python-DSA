s=input()
x=list(s)
temp=[]
for i in range(len(s)-1,-1,-1):
    temp.append(s[i])
if temp==x:
    print("YES")
else:
    print("NO")