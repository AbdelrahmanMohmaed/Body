from math import *

try :
    X = str(input(
        "Choose The calculation or Transformation for Calculation Choose >>{C} , for Choose Trans Choose >> {T}: ")).strip().capitalize()

    while X != "END":
        if X == "C":
            operator = input("Choose The operator (+ , *, /, -, sqrt) : ").strip()
            if operator == "+":
                n1 = int(input("Enter The First number : "))
                n2 = int(input("Enter The Second number : "))
                print(f"=>>  {n1 + n2} ")
            elif operator == "*":
                n1 = int(input("Enter The First number : "))
                n2 = int(input("Enter The Second number : "))
                print(f"=>>  {n1 * n2} ")
            elif operator == "-":
                n1 = int(input("Enter The First number : "))
                n2 = int(input("Enter The Second number : "))
                print(f"=>>  {n1 - n2} ")
            elif operator == "/":
                n1 = int(input("Enter The First number : "))
                n2 = int(input("Enter The Second number : "))
                print(f"=>>  {n1 / n2} ")
            elif operator == "sqrt":
                n1 = int(input("Enter The First number : "))
                print(sqrt(n1))

            else:
                  print("Not Available")

            print("Do want to Change or Not ")
            y = input("For Choose Change  >> {Change} For End Choose > {End} : ").capitalize()
            if y == "Change" :
                X = input(
                    "Choose The calculation or Transformation for Calculatoin Choose >>{C} , for Choose Trans Choose >> {T}:").strip().capitalize()
            else :
                break

        elif X == "T":
            convert = input("Choose convert from Decimal to binary {D} or Binary to decimal {B} : ").strip().capitalize()
            if convert == "B":
                n1 = str(input("Enter The number"))
                n2 = int(n1, 2)
                print(f" Your Answer is : {n2}")
            elif convert == "D":
                n1 = int(input("Enter The number"))
                print(f"Your Answer is  {bin(n1)}")

            else:
                print("wrong")
            print("Do want to Change or Not ")
            y = input("For Choose Change  >> {Change} For End Choose > {End}: ").capitalize()
            if y == "Change" :
                X = input(
                    "Choose The calculation or Transformation for Calculatoin Choose >>{C} , for Choose Trans Choose >> {T}:").strip().capitalize()
            else :
                break




        else:
            print("Thank you for using our calculator.")
            break
except :
    print("invalid input")
