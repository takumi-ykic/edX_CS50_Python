import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define the regex pattern to capture the time components
    pattern = r"^(1?\d)(?:\s*:\s*(0?[0-5]\d))? (AM|PM) to (1?\d)(?:\s*:\s*(0?[0-5]\d))? (AM|PM)$"
    result = re.search(pattern, s, re.IGNORECASE)

    if not result:
        raise ValueError("Invalid time format")

    s_hour, s_min, s_am_pm = int(result.group(1)), result.group(2) or "00", result.group(3).upper()
    e_hour, e_min, e_am_pm = int(result.group(4)), result.group(5) or "00", result.group(6).upper()

    start_hour_24 = to_24_hour(s_hour, s_am_pm)
    end_hour_24 = to_24_hour(e_hour, e_am_pm)

    formatted_s = f"{start_hour_24:02}:{s_min}"

    start_minutes = start_hour_24 * 60 + int(s_min)
    end_minutes = end_hour_24 * 60 + int(e_min)

    if end_minutes <= start_minutes:
        end_minutes += 24 * 60

    end_hour_24 = (end_minutes // 60) % 24
    end_min = end_minutes % 60

    formatted_e = f"{end_hour_24:02}:{end_min:02}"

    return f"{formatted_s} to {formatted_e}"

def to_24_hour(hour, am_pm):
    if hour == 12:  # Handle noon and midnight cases
        return 0 if am_pm == "AM" else 12
    return hour + 12 if am_pm == "PM" else hour

if __name__ == "__main__":
    main()
