import datetime
import os
x=datetime.datetime.now()
"""
# I make a new file then close this codes because when I work it finish code, then the code will show eror
# we can't open file twice time. 
os.mkdir("C:\\Date_Time")
if not os.path.exists("C:\\Date_Time"):
    os.mkdir("C:\\Date_Time")
else:
    print("Everything is okay")
"""
y="C:\\Date_Time"
file=open(y+"\\Time.txt","w")
file.write(str(x))
file.close()
