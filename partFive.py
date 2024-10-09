
def dayCheck():
    days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    userDayInput = str(input("Input day of the week: ")).casefold()
    if userDayInput == ("saturday" or "sunday"):
        print("It's the weekend!")
    elif userDayInput in days:
        print("It's a weekday.") 
    else:
        print("Invalid day of the week entered")       


if __name__ == "__main__":
    dayCheck()
