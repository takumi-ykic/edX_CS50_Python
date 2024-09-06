import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'^.*iframe src=\"(?:https?://)?(?:w{3}\.)?youtube\.com/(?:embed/)?([a-zA-Z0-9_-]{11})\".*$'

    result = re.search(pattern, s, re.IGNORECASE)

    if result:
        id = result.group(1)
        return f"https://youtu.be/{id}"
    else:
        return None

if __name__ == "__main__":
    main()
