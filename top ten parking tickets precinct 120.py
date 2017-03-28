#Which license plate got the most tickets in the my neighborhood? (120th precinct)

import csv

tickets = {}  

f = open("tickets2016.csv")
reader = csv.DictReader(f)

for row in reader:
    plate = row["Plate ID"]
    tickets[plate] = tickets.get(plate,0)+1

worst = sorted(tickets, key = tickets.__getitem__,reverse=True)

for i in range(10):
    print("plate", worst[i],"has", tickets[worst[i]],"tickets.")
