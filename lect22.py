#love calculator
name1=input("enter name 1 : ")
name2=input("enter name 2 : ")
name1_lower=name1.lower()
name2_lower=name2.lower()
combined_name=name1_lower+name2_lower
t=combined_name.count("t")
r=combined_name.count("r")
u=combined_name.count("u")
e=combined_name.count("e")
true=t+r+u+e

l=combined_name.count("l")
o=combined_name.count("o")
v=combined_name.count("v")
e=combined_name.count("e")

love=l+o+v+e

true_str=str(true)
love_str=str(love)
love_score=true_str+love_str
if int(love_score)<10 or int(love_score)>90:
    print(f"your love score is {love_score} and you go together like coke and mentos")
elif int(love_score)>=40 and int(love_score)<=50:
    print(f"you love score is {love_score} and you both are alright together")
else:
    print(f"your love score is {love_score}")