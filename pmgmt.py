# Password Management
from stdiomask import getpass
import json
import elara
import hashlib

from hasher import decode_password, encode_password, hash_master_password
from CRUD import new_password, view_password, delete_password, update_password


def set_master_password():
    master_password = getpass(prompt = "Set Master Password - ", mask = '*')
    return hash_master_password(master_password)



def intialise_db():
    db = elara.exe_secure("data.db", True)
    
    if not db.exists("Masterpassword"):
        db.set("Masterpassword", set_master_password())
    return db



def main():
    db = intialise_db()
    verify_master_password_unhashed = getpass(prompt = "Enter master password to proceed - ", mask = '*' )
    verify_master_password = hash_master_password(verify_master_password_unhashed)
    if verify_master_password == db.get("Masterpassword"): 
        print("Hi! Please select an option you want to continue with: ")
        while(1):
            print(" ")
            print("1. Add a new password")
            print("2. View a password")
            print("3. Delete a password") 
            print("4. Update a password") 
            print("5. Exit ")
            print(" ")

            choice = int(input("Enter option number - "))
            if choice == 1:
                db = new_password(db)
            elif choice == 2:
                view_password(db)
            elif choice == 3:
                db = delete_password(db)
            elif choice == 4:
                db = update_password(db)
            elif choice == 5:
                print(" ")
                print("Thank you for using our application.")
                break
            else:
                print("Invalid choice.")

            
    else:
        print("Authentication failed.")

main()