#A list which has 10 random numbers. We try to fing Odd and Even number?
import random
List=[]
Odd=[]
Even=[]

for i in range(10):
    List.append(random.randint(1,100))
for i in range(10):
    if List[i]%2==0:
        Even.append(List[i])
    else:
        Odd.append(List[i])
print(List)        
print("Even Numbers:",Even)
print("Odd Numbers:",Odd)