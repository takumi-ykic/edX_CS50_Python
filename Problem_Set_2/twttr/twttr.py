def main():
    str = input("Input: ")
    shorten(str.strip())

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]

    print("Output: ", end="")
    for s in word:
        if s.lower() not in vowels:
            print(s, end="")

    print("\n")

if __name__ == "__main__":
    main()
