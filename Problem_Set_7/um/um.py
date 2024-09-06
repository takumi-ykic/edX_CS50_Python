import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    pattern = r"\bum\b"
    result = re.findall(pattern, s, re.IGNORECASE)

    return len(result)

if __name__ == "__main__":
    main()
