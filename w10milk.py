allData=[
    ["Coffee","Water","Milk","Icecream"],
    ["Espresso","No","No","No"],
    ["Long Black","Yes","No","No"],
    ["Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes","No"],
    ["Affogato","No","No","Yes"]
]

data=allData[1:]
data

milkCount=0.0
milkB=0.0

for i in data:
    if i[2].upper()=='YES':
        milkCount += 1
milkB =milkCount/len(data)
milkB