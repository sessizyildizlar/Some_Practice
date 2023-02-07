def Pr_nb(x):
    if x==1:
        return False
    if x==2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True

x=int(input("Write a number:"))
if Pr_nb(x)==True:
    print("This number is Prime Number")
else:
    print("This isn't a Prime Number")