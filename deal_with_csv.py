import unicodecsv

enrollments = []
f = open('enrollments.csv', 'rb')
reader = unicodecsv.DictReader(f)

i = 0
for row in reader:
    enrollments.append(row)
    print enrollments[i]
    i = i+1
f.close()

