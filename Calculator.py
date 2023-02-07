def Calc(Oprt,x,y):
    while True:
        if Oprt =="+":
            return x+y
            break
        elif Oprt =="-":
            return x-y
            break
        elif Oprt =="/":
            return x/y
            break
        elif Oprt =="*":
            return x*y
            break
        else:
            print("You should choice true operation!")
            continue

print("Hello! Welcome calculater")
Oprt=input("Please take a operation 1=+,2=-,3=/,4=* : ")
x=int(input("Write first number:"))
y=int(input("Write second number:"))
print(Calc(Oprt,x,y))