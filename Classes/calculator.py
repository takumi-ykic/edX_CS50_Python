# x = int(input("What's x? "))
# y = int(input("What's y? "))
# z = int(x) + int(y)

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)
# z = round(x / y, 2)
# z = x / y

# print(f"{z:,}")

# print(f"{z:.2f}")


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    # return n ** 2
    return pow(n, 2)

    #For Unit test
    # return n + n

if __name__ == "__main__":
    main()