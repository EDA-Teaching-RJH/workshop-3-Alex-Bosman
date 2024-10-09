
def moviePrice():
    studentQuery = str(input("are you a student (yes/no): ")).casefold()
    age = int(input("enter your age: "))

    if (studentQuery == "yes") and (12 <= age <= 64):
        print("£8")
    elif (age > 12) or (age <= 65):
        print("£5")
    elif 12 <= age <= 64:
        print("£10")
    else:
        print("invalid entry")


if __name__ == "__name__":
    moviePrice()