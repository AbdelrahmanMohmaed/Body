from math import *  # sqrt >>>>

X = input("Choose The calculation or Transformation:").strip().capitalize()

while X == "C":
    operator = input("Choose The operator").strip()
    if operator == "+":
        n1 = int(input("Enter The First number"))
        n2 = int(input("Enter The Second number"))
        print(f"=>>  {n1 + n2} ")
    elif operator == "*":
        n1 = int(input("Enter The First number"))
        n2 = int(input("Enter The Second number"))
        print(f"=>>  {n1 * n2} ")
    elif operator == "-":
        n1 = int(input("Enter The First number"))
        n2 = int(input("Enter The Second number"))
        print(f"=>>  {n1 - n2} ")
    elif operator == "/":
        n1 = int(input("Enter The First number"))
        n2 = int(input("Enter The Second number"))
        print(f"=>>  {n1 / n2} ")
    elif operator == "sqrt":
        n1 = int(input("Enter The First number"))
        print(sqrt(n1))
    elif operator == "END":
        break
    elif operator == "Change" :
        X = input("Choose The calculation or Transformation:").strip().capitalize()


    else:
        print("Not Available")
        operator = input("Choose The operator").strip()
else:
    if X == "T":
        convert = input("Choose convert from Decimal to binary {D} or Binary to decimal {B}").strip()
        if convert == "D":
            n1 = str(input("Enter The number"))
            n2 = int(n1, 2)
            print(f" Your Answer is : {n2}")
        elif convert == "B":
            n1 = int(input("Enter The number"))
            print(f"Your Answer is  {bin(n1)}")
        else :
            print("Wrong")
