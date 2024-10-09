

def askAge():
    age = int(input("input age: "))
    if age >= 18:
        print("You are an adult")
    elif age >= 0:
        print("You are a child")
    else:
        print("invalid age entered")



if __name__ == "__main__":
    askAge()