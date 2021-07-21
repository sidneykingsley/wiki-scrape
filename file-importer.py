import csv
with open('musician-names.csv', newline='') as f:
    reader = csv.reader(f)
    names = list(reader)
for x in names:
    fname = x[0]
    sname = x[1]
    sname = sname.strip()