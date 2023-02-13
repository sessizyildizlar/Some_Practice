Fruit_Wholesaler=["Apple","Pear","Peach","Banana","Watermelon"]
Veg_Wholesaler=["Carrot","Tomatoes","Leek","Pepper"]
F_Supplier=[]
V_Supplier=[]
Customer=[]
F_Kilos=[]
V_Kilos=[]
kilos1=0
kilos2=0
kilos3=0
kilos4=0

while True:
    print("Welcome Wholesaler Store")
    Ask=input("If you want to buy fruit, Please write F, or you want buy Vegatable, please write V: ").upper()
    if Ask=="F":
        print(Fruit_Wholesaler)
        choice=input("Which one do you want to buy?: ").lower()
        F_Supplier.append(choice)
        kilos1=int(input("How much kilos do you want to buy?: "))
        F_Kilos.append(kilos1)
        Question=input("Do you want to continue to buy? (Y or N): ").upper()
        if Question=="Y":
            continue
        elif Question=="N":
            break
    elif Ask=="V":
        print(Veg_Wholesaler)
        choice2=input("Which one do you want to buy?: ").lower()
        V_Supplier.append(choice2)
        kilos2=int(input("How much kilos do you want to buy?: "))
        V_Kilos.append(kilos2)
        Question2=input("Do you want to continue to buy? (Y or N): ").upper()
        if Question2=="Y":
            continue
        elif Question2=="N":
            break


while True:
    print("Welcome Market")
    Ask=input("If you want to buy Fruit, please write F, If you want to buy vegetable, write V: ").upper()
    if Ask=="F":
        print(F_Supplier)
        choice=input("Which one do you want to buy: ").lower()
        N1=F_Supplier.index(choice)
        N2=F_Kilos[N1]
        kilos3=int(input("How much kilos?: "))
        if kilos3<N2:
            Customer.append(choice)
            N2=N2-kilos3
            F_Kilos[N1]=N2
            Question3=input("Do you want to continue? (Y or N): ").upper()
            if Question3=="Y":
                continue
            elif Question3=="N":
                print("You are buying:",Customer)
                break
        elif kilos3>N2:
            print("We cant give you this fruit for this quantity")
            Question4=input("Do you want to continue? (Y or N): ").upper()
            if Question4=="Y":
                continue
            elif Question4=="N":
                print("You are buying:",Customer)
                break
    elif Ask=="V":
        print(V_Supplier)
        choice=input("Which one do you want to buy?: ").lower()
        kilos4=int(input("How much kilos?: "))
        N1=V_Supplier.index(choice)
        N2=V_Kilos[N1]
        if kilos4<N2:
            Customer.append(choice)
            N2=N2-kilos4
            V_Kilos[N1]=N2
            Question5=input("Do you want to continue? (Y or N): ").upper()
            if Question5=="Y":
                continue
            elif Question5=="N":
                print("You are buying:",Customer)
                break
        elif kilos4>N2:
            print("We cant give this fruit for this quantity")
            Question6=input("Do you want to continue? (Y or N): ").upper()
            if Question6=="Y":
                continue
            elif Question6=="N":
                print("You are buying:",Customer)
                break

