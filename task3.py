Users = {
    "Abdo": {"PassWord": "123", "ID": "30304080100099"},
    "Mona": {"PassWord": "456", "ID": "20203038800068"},
    "Mahmoud": {"PassWord": "789", "ID": "30106051400077"}
}
Governorate = {
    "01" : "Cairo",
    "02" : "Alexandria",
    "03" : "port said" ,
    "04": "Suez",
    "11": "Damietta",
    "12": "Dakahlia",
    "13": "Elsharqia",
    "14": "Qalyubia",
    "15": "Kafr El-Sheikh",
    "16": "Elgharbia",
    "17": "Menoufia",
    "18": "Elbehira",
    "19": "Ismailia",
    "21": "Giza",
    "22": "Beni Suef",
    "23": "Fayoum",
    "24": "Minya",
    "25": "Assiut",
    "26": "Sohag",
    "27": "Qena",
    "28": "Aswan",
    "29": "Luxor",
    "31": "Red Sea",
    "32": "El wady elgedeed",
    "33": "Matrouh",
    "34": "North Sinai",
    "35": "South Sinai"
}




try:
    User_Name = str(input("Enter Your User Name : ")).strip().capitalize()
    PW = input("Enter Your User Password : ")
    ID = Users[User_Name]["ID"]
    Year_of_Birth = Users[User_Name]["ID"][1:3]
    Day_Of_Birth = Users[User_Name]["ID"][5:7]
    Month_Of_Birth = Users[User_Name]["ID"][3:5]
    Governorate_code = Users[User_Name]["ID"][7:9]
    Male_Or_Female = int(Users[User_Name]["ID"][12:13])
    Century = int(Users[User_Name]["ID"][0])

    # Loop

    while User_Name in Users and PW == Users[User_Name]["PassWord"]:
        print(
            f"Your ID is {ID} \nThe Day You Was Born is : {Day_Of_Birth}\nThe Month You born in is : {Month_Of_Birth}\nThe Year You Born in : {Year_of_Birth}")
        if Governorate_code == "88":
            print(f"The Governorate_code is : {Governorate_code} , You Don't Born in Egypt")
        elif Governorate_code in Governorate :
            print(f"The Code of  Governorate is {Governorate_code}  and You From {Governorate[Governorate_code]} ")
        if Century == 2:
            print("You Born in Century 20")
        elif Century == 3:
            print("You Born in Century 21")

        if Male_Or_Female % 2 == 0:
            print("Female")
        else:
            print("Male")
        print("Do You Want To Continue With another User or End For Continue Choose >> C For End >>  E")
        X = (input("Enter C Or E : "))
        if X == "E":
            break
        elif X == "C":
            User_Name = str(input("Enter Your User Name : ")).strip().capitalize()
            PW = input("Enter Your User Password : ")


    else:
        print("The User name or Password are Wrong")
except:
    print("invaild Value")
