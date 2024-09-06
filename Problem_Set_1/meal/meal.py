import math

def main():
    time = input("What time is it? ")
    time = time.strip()

    time_converted = convert(time)

    if (7 <= time_converted and time_converted <= 8):
        print("breakfast time")
    elif (12 <= time_converted and time_converted <= 13):
        print("lunch time")
    elif (18 <= time_converted and time_converted <= 19):
        print("dinner time")

def convert(time):
    hour, minutes = time.split(":")
    hour = float(hour)
    minutes = float(minutes) / 60

    converted = hour + minutes
    return converted

if __name__ == "__main__":
    main()
