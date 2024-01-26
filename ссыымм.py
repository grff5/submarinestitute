import csv
with open("03_2057.csv", "r", encoding = "utf-8", newline="") as f:
    reader = csv.reader(f, delimiter = ",")
    rows = list(reader)

m=0
for i in range(1, len(rows)):
    m=max(m, int(rows[i][4]))
print(m)
