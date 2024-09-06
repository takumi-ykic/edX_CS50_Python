import sys

def main():
    str = input("Input: ")
    twttr = shorten(str.strip())
    print(twttr)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    twttr = ""

    if word.isnumeric():
        sys.exit(1)

    for s in word:
        if not s.lower() in vowels:
            twttr += s

    return twttr

if __name__ == "__main__":
    main()
