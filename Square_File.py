import os
"""
#Firtsly you should work this part then close this. After that you have to work on second part
os.mkdir("C:\\Square")
if not os.path.exists("C:\\Square"):
    os.mkdir("C:\\Square")
else:
    print("Everything is okay")
"""
#SECOND PART
x="C:\\Square"
file=open(x+"\\Square_Calculator.txt","w")
square=0
start=int(input("What is your start point: "))
end=int(input("What is your end point: "))
for i in range(start,end+1):
    square=i**2
    file.write(str(i)+" Number square is :"+str(square)+"\n")
file.close()
