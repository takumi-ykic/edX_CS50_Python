import sys
import csv

if len(sys.argv) < 3:
    exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    exit("Too many command-line arguments")
else:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    if (arg1[-4:] == ".csv") and (arg2[-4:] == ".csv"):
        try:
            path = open(arg1)
        except FileNotFoundError:
            sys.exit(f"Could not read {arg1}")
        else:
            list = []
            with path as file:
                reader = csv.DictReader(file)
                for row in reader:
                    x, y = row["name"].split(",")
                    list.append({"first": y, "last": x, "house": row["house"]})

            with open(arg2, "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for i in range(len(list)):
                    writer.writerow({"first": list[i]["first"], "last": list[i]["last"], "house": list[i]["house"]})
    else:
        sys.exit("Not a CSV file")
