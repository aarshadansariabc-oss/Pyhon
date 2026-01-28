from pathlib import Path
import os


# This Funciton is to check the total file and folder within the file
def Total_file_Folder():
    path = Path('.')
    all_items = list(path.rglob('*'))

    for i, item in enumerate(all_items, start=1):
        print(f"{i} : {item}")



# This function if for to create the file
def create_File():
    try:
        Total_file_Folder()
        name = input("Enter the name of the file : ")
        p = Path(name)

        if not p.exists():
            with open(p, 'w') as fs:
                data = input("What do you want to write in this file : ")
                fs.write(data)

            print("File Create Successfully!")
        else:
            print("File Already exist")

    except Exception as err:
        print(f"An error occured {err}")


# This funciton is to read the file
def read_file():
    try:
        Total_file_Folder()
        name = input("Enter the name of the file : ")
        p = Path(name)
        if p.exists():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("File readed successfull")
        else:
            print("File does not exits")

    except Exception as err:
        print(f"An error occures {err}")



# This funciton is used to update the file
def update_file():
    try:
        Total_file_Folder()
        name = input("Which file you wanted to update : ")
        p = Path(name)
        if p.exists():
            print("Press 1 for chnage your file name : ")
            print("Press 2 for overwrite you file : ")
            print("Press 3 to appent something in your file : ")
            u_choice = int(input("Enter your chocie : "))

            if u_choice == 1:
                name2 = input("Enter your new file name : ")
                p2 = Path(name2)
                p.rename(p2)

            if u_choice == 2:
                with open(p, 'w') as fs:
                    data = input(
                        "Enter your data to overwrite in your file : ")
                    fs.write(data)

            if u_choice == 3:
                with open(p, 'a') as fs:
                    data = input("Enter your data to append : ")
                    fs.write(data)

    except Exception as err:
        print(f"An error occured {err}")


# This funciton is used to delte the file
def delete_file():
    try:
        Total_file_Folder()
        name = input("Enter your file name to delete : ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print("File delete successfully")
        else:
            print("File does not exists")

    except Exception as err:
        print(f"An error occured {err}")


print("Press 1 to Create a  file : ")
print("Press 2 to Read a  file : ")
print("Press 3 to Updating a  file : ")
print("Press 4 to Delete a  file : ")

choice = int(input("Enter Your Choice : "))


if choice == 1:
    create_File()

elif choice == 2:
    read_file()

elif choice == 3:
    update_file()

elif choice == 4:
    delete_file()

else:
    print("Invalid Choice ")
