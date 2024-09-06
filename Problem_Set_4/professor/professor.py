import random

def main():
    level = get_level()
    num_questions = 10
    score = 0
    for _ in range(num_questions):
        x = generate_integer(level)
        y = generate_integer(level)
        count = 0
        while count < 3:
            answer = input(f"{x} + {y} = ")
            if not answer.isdigit():
                print("EEE")
                count += 1
                if count == 3:
                    print(f"{x} + {y} = {x + y}")
            else:
                answer = int(answer)
                if answer != (x + y):
                    print("EEE")
                    count += 1
                    if count == 3:
                        print(f"{x} + {y} = {x + y}")
                else:
                    score += 1
                    break
    print(f"Score: {score}")
def get_level():
    level = None
    while True:
        level = input("Level: ")
        if level.isdigit():
            level = int(level)
            if level in [1,2,3]:
                return level


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)

if __name__ == "__main__":
    main()
