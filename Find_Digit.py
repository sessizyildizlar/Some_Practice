
Number=int(input("Please right a number! : "))
x=0
y=Number
if Number<10:
    print(f"{Number} number has 1 digit")
else:
    while Number>=10:
        Number=Number//10
        x+=1
        if Number<10:
            x+=1
            break
    print(f"{y} number has {x} digit!")