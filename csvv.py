# Create a python code to read from a CSV file of student marks and calculate average marks.

import csv

file=open ("students.csv","w")
writer= csv.writer(file)

writer.writerow(["name","marks"])
writer.writerow(["Suhana",60])
writer.writerow(["Sita",70])
writer.writerow(["Hari",80])

file.close()
print("File Created")

file=open("students.csv","r")
reader=csv.DictReader(file)

totalMarks=0
n=0

for row in reader:
    totalMarks+=float(row["marks"])
    n += 1

file.close()

average=totalMarks/n
print("Total Students:", n)
print("Average Marks:", average)

print("Suhana Paudel")
