import sys
import csv
import tabulate

path = None

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2:
    path = sys.argv[1]
else:
    sys.exit("Too many command-line arguments")

if path[-4:] == ".csv":
    try:
        csv_file = open(path)
    except FileNotFoundError:
        exit("File does not exist")
    else:
        list = []
        with csv_file as file:
            reader = csv.reader(file)
            for row in reader:
                list.append(row)

            print(tabulate.tabulate(list, headers="firstrow", tablefmt="grid"))
else:
    sys.exit("Not a CSV file")
