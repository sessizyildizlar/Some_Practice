#We will try to make pyramid by stars.

x=int(input("How many lines do you want to see in pyramid?"))
y=1
for i in range(1,x):
    print(x*" ","*"*(y)," "*x)
    x-=1
    y+=2
