from datetime import date
import inflect
import sys

def main():
    try:
        input_date = input("Date of Birth: ")

        today = date.today()
        dob = date.fromisoformat(input_date)
        gap = today - dob

        print(convert(gap.days))
    except ValueError:
        sys.exit("Invalid date")

def convert(time):
    minutes = time * 24 * 60
    inflector = inflect.engine()

    return inflector.number_to_words(minutes, andword='').capitalize() + " minutes"

if __name__ == "__main__":
    main()
