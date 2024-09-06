msg = input("camelCase: ")

print("snake_case: ", end="")

for char in msg:
    if char.isupper():
        char = "_" + char.lower()
        print(char, end="")
    else:
        print(char, end="")
print("\n")

