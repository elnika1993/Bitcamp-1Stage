import random

while True:
    try:
        level = int(input("level: "))
        if level > 0:
            break
    except:
        continue

x = random.randint(1, level)


while True:
    try:
        guess = int(input("Guess: "))
        if guess > x:
            print("Lower")
        elif guess < x:
            print("Higher")
        else:
            print("You Are Right!")
            break
    except ValueError:
        continue
    