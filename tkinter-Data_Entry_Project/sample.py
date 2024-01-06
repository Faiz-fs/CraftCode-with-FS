import csv
import datetime

filename = str(datetime.date.today())
path = "data/"
details = []
with open(path + filename, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        details.append(tuple(row))

print(details)
