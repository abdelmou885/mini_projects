def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("/")
            print(f"Username:{user}\nPassword:{passw}")
def get_user_data(name):
    with open("password.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("/")
            if user==name:
                print(user,passw)
get_user_data("ahmed")