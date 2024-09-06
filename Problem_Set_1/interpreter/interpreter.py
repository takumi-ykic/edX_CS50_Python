exp = input("Expression: ")
exp = exp.strip()
x, y, z = exp.split(" ")

x = int(x)
z = int(z)
total = 0.0

match y:
    case "+":
        total = float(x + z)
    case "-":
        total = float(x - z)
    case "*":
        total = float(x * z)
    case "/":
        total = float(x / z)

print(format(total, ".1f"))
