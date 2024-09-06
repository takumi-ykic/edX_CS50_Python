import random
import sys

from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if not len(sys.argv) in (1, 3):
    print("Invalid usage")
    sys.exit(1)

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
elif len(sys.argv) == 3:
    if sys.argv[1] not in ("-f", "--font"):
        print("Invalid usage")
        sys.exit(1)
    if sys.argv[2] in fonts:
        font_sel = sys.argv[2]
        figlet.setFont(font=font_sel)
    else:
        print("Invalid usage")
        sys.exit(1)

userin = input("Input: ")

print(figlet.renderText(userin))
