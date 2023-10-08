import random
n = random.randrange(1,11)
The_Guessing_Number = int(input("Guess The Number :"))
Tries = 4
while The_Guessing_Number != n:
    if The_Guessing_Number > n:
        print(f"Your number is higher , Correct Number is Lower Than {The_Guessing_Number}")
        Tries -= 1
        print(f"You Have only  {Tries} Chances left  ")
        The_Guessing_Number = int(input("Guess The Number :"))
        if Tries == 1:
            print("You Finish Your Chance")
            break
    else:
        print(f"Your Number is Lower,  Correct Number is Higher Than {The_Guessing_Number}")
        Tries -= 1
        print(f"You Have only  {Tries} Chances left ")
        The_Guessing_Number= int(input("Guess The Number"))
        if Tries == 1:
            print(" Wrong, You Finish Your Chance")
            break

else:
    print(" Correct, Bravo :D")
