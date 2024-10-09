
def gradeCalc():
    grade = int(input("Input number grade: "))
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    elif 0 <= grade <= 59:
        print("F")
    else:
        print("Invalid Grade input")


if __name__ == "__main__":
    gradeCalc()