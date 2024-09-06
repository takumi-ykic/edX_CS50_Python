import sys
from PIL import Image, ImageOps

def main():
    extensions = ["png", "jpg", "jpeg"]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        extension1 = arg1.split(".")[-1].lower()
        extension2 = arg2.split(".")[-1].lower()
        if ((extension1 in extensions) and (extension2 in extensions)):
            if extension1 != extension2:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")

        try:
            shirt = Image.open("shirt.png")
            size = shirt.size
            before_img = Image.open(arg1)
        except FileNotFoundError:
            sys.exit("Input does not exist")
        else:
            before_img = ImageOps.fit(before_img, size)
            before_img.paste(shirt, shirt)
            before_img.save(arg2, format=None)

if __name__ == "__main__":
    main()



