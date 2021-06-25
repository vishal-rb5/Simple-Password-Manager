from hasher import decode_password, encode_password, hash_master_password
import elara
from stdiomask import getpass

def new_password(db):
    
    website = input("Enter website for which password must be saved - ")
    password = getpass(prompt = "Enter password to be saved - ", mask = '*')
    db.set(website, encode_password(password))
    print("Password added succesfully.")
    return db


def view_password(db):
    print("Websites for which passwords have been saved: ")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j, ". ", i)
        j+=1
        
    index = int(input("Enter website serial no. for which password is to be viewed - "))
    if index>0 and index<=len(keys): 
        print("Password - ",decode_password(db.get(keys[index-1])))

    
def delete_password(db):
    print("Websites for which passwords have been saved: ")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j, ". ", i)
        j+=1
    
    index = int(input("Enter website serial no. for which password is to be deleted - "))
    verify_master_password_unhashed = getpass(prompt = "Enter master password for verification - ", mask = '*')
    verify_master_password = hash_master_password(verify_master_password_unhashed)
    if verify_master_password == db.get("Masterpassword"):
        if index>0 and index<=len(keys):
            db.rem(keys[index-1])
            # Del website and password from dict
            print("Password deletion succesful.")
    else:
        print("Authentication failed. Password not deleted.")

    return db

def update_password(db):
    print("Websites for which passwords have been saved: ")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j, ". ", i)
        j+=1
    
    index = int(input("Enter website serial no. for which password is to be updated - "))
    verify_master_password_unhashed = getpass(prompt = "Enter master password for verification - ", mask = '*')
    verify_master_password = hash_master_password(verify_master_password_unhashed)
    if verify_master_password == db.get("Masterpassword"):
        if index>0 and index<=len(keys):
            newpass = getpass(prompt = "Enter new password - ", mask = '*')
            db.set(keys[index-1], encode_password(newpass))
            print("Password updated succesful.")
            
        else:
            print("Authentication failed. Password not updated.")

    return db
