import math
print("Enter the amount of money to get change of")
change = input("")
if isinstance(change, str):
    print("BROOOO WHAT YOU DOIN??? A FLOAT, IDIOT!")
    exit()
else:
    cents = math.floor(100*float(change))
print(cents)
print("Which currency are we using? Euro, Dollar, or BTC")
currency = input()