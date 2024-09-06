def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    if "$" in d:
        d = d.replace("$", "")
    d.strip()
    return float(d)

def percent_to_float(d):
    if "%" in d:
        d = d.replace("%", "")
    d.strip()
    d = float(d)
    return d / 100

main()
