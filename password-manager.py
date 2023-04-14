from cryptography.fernet import Fernet

def write_key():
    key=Fernet.generate_key()
    with open("keys.key","wb") as key_files:
        key_files.write(key)

#write_key()


def load_keys():
    with open("keys.key","rb") as key_file:
        key=key_file.read()
    return key

def decrypted_pwd(encrypted_pwd,key):
    fernet=Fernet(key)
    decrypted_pwd=fernet.decrypt(encrypted_pwd.encode())
    return decrypted_pwd.decode()

def encrypted_pwd(password,key):
    fernet=Fernet(key)
    encrypted_pwd=fernet.encrypt(password.encode())
    return encrypted_pwd.decode() 

def add_pwd():
    name=input("Account name: ")
    pwd=input("Password: ")
    key=load_keys()
    encrypted_password=encrypted_pwd(pwd,key)
    with open("passwords.txt","a") as f:
        f.write(name+"|"+encrypted_password+"\n")

    print("password added sucessfully")

def view_pwd():
    key=load_keys()
    with open("passwords.txt","r") as f:
        for line in f:
            name,encrypted_pwd=line.strip().split("|")
            password=decrypted_pwd(encrypted_pwd,key)
            print("Account name:",name,"|","password:",password)

while True:
    mode=input("Would you like to add a new password or view the existing passwords? (view,add,press q to quit): ")
    if mode=="q":
        break
    if mode=="add":
        add_pwd()
    elif mode=="view":
        view_pwd()
    else:
        print("Invalid mode")