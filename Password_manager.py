from cryptography.fernet import Fernet
import sys
"""
def write_key():
    key = Fernet.generate_key()
    with open("key.txt","wb") as key_file :
        key_file.write(key)
"""
def load_key():
    file=open("key.txt","rb")
    key=file.read()
    file.close()
    return key

master_pwd=input("Enter your password:").lower()
if master_pwd=="abdel":
    print("Welcome to Password Manager")
else:
    sys.exit("access denied ")
key=load_key() + master_pwd.encode()
fer=Fernet(key)

def view(name):
    with open("password.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("/")
            if user==name:
                passw=fer.decrypt(passw.encode()).decode()
                return user,passw
        return False

# noinspection PyTypeChecker
def add():
    name=input("Enter your name: ")
    pwd=input("Enter your password: ")
    with open("password.txt","a") as f:
        f.write(name+"/"+fer.encrypt(pwd.encode()).decode()+"\n")

while True:
    mode=input("What would you like to view or add a passawoed? / enter q to quit: ").lower()
    if mode=='q':
        break
    if mode=="view":
        w=input("what is your name?: ").lower()
        isfound=view(w)
        if isfound==False:
            print("not found")
        else:
            print(isfound)
    elif mode=="add":
        add()
    else:
        print("Invalid input")
        continue
