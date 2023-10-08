from math import *

X = input("Choose The calculation or Transformation:").strip().capitalize()

while X != "END":
    if X == "C":
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
        elif operator == "Change":
            X = input("Choose The calculation or Transformation:").strip().capitalize()
        else:
            print("Not Available")
    elif X == "T":
        convert = input("Choose convert from Decimal to binary {D} or Binary to decimal {B}").strip().capitalize()
        if convert == "B":
            n1 = str(input("Enter The number"))
            n2 = int(n1, 2)
            print(f" Your Answer is : {n2}")
        elif convert == "D":
            n1 = int(input("Enter The number"))
            print(f"Your Answer is  {bin(n1)}")
        elif convert == "Change".capitalize():
            X = input("Choose The calculation or Transformation:").strip().capitalize()
        else:
            print("wrong")


    else:
        print("Thank you for using our calculator.")
        break
