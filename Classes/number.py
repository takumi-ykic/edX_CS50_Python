def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            break
        except ValueError:
            print("x is not an integer")
            # pass
        # else:
        #     break
        
    return x


# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print("x is not an integer")
#     # else:
#     #     break
        
# print(f"x is {x}")

main()







