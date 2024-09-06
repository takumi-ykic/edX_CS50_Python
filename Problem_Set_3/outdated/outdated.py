months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6 ,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            mon, day, year = date.split("/")
            if not mon.strip().isdigit():
                raise ValueError
        elif " " in date:
            mon, day, year = date.split(" ")

        mon = mon.strip()
        day = day.strip()
        year = year.strip()

        if mon.isdigit():
            mon = int(mon)
            if not (1 <= mon <= 12):
                raise ValueError
        else:
            mon = mon.capitalize()
            if mon in months:
                if "," in day:
                    mon = months[mon]
                else:
                    raise ValueError
            else:
                raise ValueError

        if "," in day:
            day = day.replace(",", "")

        if not day.isdigit():
            raise ValueError
        else:
            day = int(day)
            if not(1 <= day <= 31):
                raise ValueError

        if year.isdigit():
            if len(year) > 4:
                raise ValueError
            else:
                year = int(year)
        else:
            raise ValueError

        break
    except ValueError:
        ...

result = f"{year:04}-{mon:02}-{day:02}"
print(result)


















