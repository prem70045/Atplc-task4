import random

number = random.randint(1, 9)

while True:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == number:
        print("Correct!")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high.")
