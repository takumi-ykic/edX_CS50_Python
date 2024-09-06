def main():
    print(gauge(convert(input("Fraction: "))))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            return round(int(x) / int(y), 2) * 100
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def gauge(percentage):
    percentage = int(percentage)
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif percentage > 100:
        main()
    else:
        return f"{format(percentage, ".0f")}%"

if __name__ == "__main__":
    main()
