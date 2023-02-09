def Calc():
    N1=int(input("Number1: "))
    N2=int(input("Number2: "))
    Opr=input("Operations(+,-,/,*)")
    assert Opr=="+" or Opr=="-" or Opr=="/" or Opr=="*"
    if Opr=="+":
        print(N1+N2)
    elif Opr=="-":
        print(N1-N2)
    elif Opr=="/":
        print(N1/N2)
    elif Opr=="*":
        print(N1*N2)
try:
    Calc()
except ValueError:
    print("Value Eror!")
except ZeroDivisionError:
    print("You can't division zero")