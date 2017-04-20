import csv
f = open("311data.csv")
reader=csv.DictReader(f)
number = {}
for row in reader:
    complaints = row["Complaint Type"]
    number[complaints]=number.get(complaints,0)+1
  
topten=sorted(number,key=number.__getitem__,reverse=True)
for i in range(10):
    print("There are", number[topten[i]], "complaints for", topten[i])
