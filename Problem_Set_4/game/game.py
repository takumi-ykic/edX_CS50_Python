import random
level = 0
target = 0
while True:
    try:
        level = int(input("Level: "))
        target = random.randint(1, level)
        break
    except ValueError:
        ...

while True:
    try:
        guess = int(input("Guess: "))
        if target == guess:
            print("Just right!")
            break
        elif target < guess:
            print("Too large!")
            raise ValueError
        elif target > guess:
            print("Too small!")
            raise ValueError
    except ValueError:
        ...


