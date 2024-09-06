import re

name = input("What's your name? ").strip()

# if "," in name:
#     last, first = name.split(",")
#     name = f"{first} {last}"

matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
