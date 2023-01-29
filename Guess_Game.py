#Question: You have 3 chance for find right number around 1-100 number
import random
x=random.randint(1,100)

for i in range(3):
    Guess=int(input("What's your guess?"))
    if (Guess==x):
        print("Congratulations!")
        break
    elif(Guess>x):
        print("Try Again!")
        print("You can try to write lower number!")
    elif(Guess<x):
        print("Try Again!")
        print("You can try to write upper number!")
print("Your chance is finish!")
print("True number is:",x)
