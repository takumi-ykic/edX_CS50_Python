# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")

# def main():
#     # print_column(3)
#     # print_row(4)
#     print_square(3)

# def print_square(size):
#     # Print row
#     for i in range(size):
#         # Print bricks
#         # for j in range(size):
#         #     print("X", end="")
#         # print()
#         print("#" * size)

# def print_row(width):
#     print("?" * width)

# def print_column(height):
#     # for _ in range(height):
#     #     print("#")
#     print("#\n" * height, end="")

# main()

# Debugging
def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        # print(i, end=" ")
        print("#" * (i + 1))

if __name__ == "__main__":
    main()

