import csv

with open('./Data/currency.csv', 'r') as file:
    lines = csv.reader(file)
    # header = next(lines)
    for line in lines:
        if 'Bangladeshi Taka' in line[0]:
            Bdtrate = line

#Convert USD to BDT
bdt = float(Bdtrate[3])
x = float(input('Enter USD: '))
def USD_to_BDT(usd,bdt):
    return usd * bdt
 
result = USD_to_BDT(x,bdt)
print(f'{x} USD to BDT {result} Taka')

#Convert BDT to USD
usd = float(Bdtrate[2])
BDT = float(input('Enter BDT: '))
def USD_to_BDT(usd,bdt):
    return usd * bdt
 
result = USD_to_BDT(usd, BDT)
print(f'{BDT} BDT to USD {result} Dolars')
    # print(header)