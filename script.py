import csv
with open('perform-summary.csv', 'rb') as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)
    break