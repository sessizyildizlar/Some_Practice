#Question: 10 Number is getting user then will find avarage of list.
List=[]
y=0
for i in range(10):
    x=float(input("Could you write a number:"))
    List.append(x)
    y=y+List[i]
print("Avarage: ",y/len(List))
