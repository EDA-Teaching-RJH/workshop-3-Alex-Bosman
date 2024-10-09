import random

def numberGuess():
    numberToGuess = random.randint(1, 10)
    guessFlag = False
    guessCounter = 1
    while not guessFlag:
        guessed = int(input("Input a number between 1 and 10: "))
        if 1 <= guessed <= 10:
            if guessed == numberToGuess:
                print(f"Number has been sucessfully guessed in {guessCounter} Attempts")
                guessFlag = True
            elif guessed > numberToGuess:
                print("Too high")
            else:
                print("Too low")
        else:
            print("Invalid input")
        guessCounter += 1



if __name__ == "__main__":
    numberGuess()