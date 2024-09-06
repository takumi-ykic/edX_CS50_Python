import inflect

p = inflect.engine()
names = []
try:
    while True:
        name = input("Name: ")
        if not name:
            break
        else:
            names.append(name)
except EOFError:
    msg = "Adieu, adieu, to "
    if len(names) == 1:
        msg += names[0]
    elif len(names) == 2:
        msg += f"{names[0]} and {names[1]}"
    else:
        msg += ", ".join(names[:-1]) + f", and {names[-1]}"

    print(msg)






