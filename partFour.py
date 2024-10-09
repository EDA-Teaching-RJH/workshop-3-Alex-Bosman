
#username : password
accounts = {"admin": "password123"}

def checkDetails():
    inputUsername = str(input("Input Username: "))
    inputPassword = str(input("Input Password: "))

    if inputUsername in accounts.keys():
        if accounts[inputUsername] == inputPassword:
            print("Access Granted")
        else:
            print("Error Access Denied")
    else:
        print("Error Invalid Username")


if __name__ == "__main__":
    checkDetails()