import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    initials = s[0:2]
    if len(initials) != 2:
        return False

    if not initials.isdigit():
        rest = s[2:]
        if len(rest) > 4:
            return False
        isNum = False
        for r in rest:
            if r.isdigit():
                if not isNum:
                    isNum = True
                    if r == '0':
                        return False
            elif isNum:
                return False

        for r in rest:
            if r == " " or r == "." or r in string.punctuation:
                return False
    else:
        return False

    return True

if __name__ == "__main__":
    main()
