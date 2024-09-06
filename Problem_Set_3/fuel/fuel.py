while True:
    try:
        str = input("Fraction: ")
        x, y = str.split("/")
        x = int(x)
        y = int(y)

        if x > y:
            continue

        result = x / y

        if result <= 0.01:
            print("E")
        elif result >= 0.99:
            print("F")
        else:
            print(f"{format(result * 100, ".0f")}%")
        break
    except ValueError:
        ...
    except ZeroDivisionError:
        ...







