#Ask user for their name
# name = input("What's your name? ")

# Remove whitespace from str
# name = name.strip()

# Capitalize first character
# name = name.capitalize()

# Capitalize user's name
# name = name.title()

# name = input("What's your name? ").strip().title()

#Split user name
# first, last = name.split(" ")

#Say hello to user
"""
It's multiple lines of comments
"""
# print("hello, " + name)
# print("hello,", name)

# print("hello, ", end="")
# print(name)
# print('Hello, "friend"')
# print("Hello, \"friend\"")
# print(f"hello, {first}")

# def hello(to="world"):
#     print("hello", to)

# hello()
# name = input("What's your name? ")
# hello(name)

def main():
    name = input("What's your name? ")
    hello(hello(name))

def hello(to="world"):
    return f"hello, {to}"

main()