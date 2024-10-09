
def userCalc():
    while True:
        a = str(input("input your first number: "))
        if a == "quit":
            break
        b = str(input("input your second number: "))
        if b == "quit":
            break
        operation = str(input("input the operation (+, -, *, /, ^, %): "))
        if (operation) == "quit":
            break
        try:
            a = float(a)
            b = float(b)
        except:
            print("invalid number entered")
            break
        match operation:
            case "+":
                answer = a + b
                print(f"Answer: {answer}")
            case "-":
                answer = a - b
                print(f"Answer: {answer}")
            case "*":
                answer = a * b
                print(f"Answer: {answer}")
            case "/":
                if b == 0:
                    print("Divide by zero Error")
                else:
                    answer = a / b
                    print(f"Answer: {answer}")
            case "^":
                answer = a ** b
                print(f"Answer: {answer}")
            case "%":
                answer = a % b
                print(f"Answer: {answer}")
            case _:
                print("Invalid Operation entered")


if __name__ == "__main__":
    userCalc()
