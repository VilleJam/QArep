per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
money = float(input())
banks = list(per_cent.keys())
i = int(len(banks))
deposit = []
k=0
while k<i:
    deposit.append(money+money/100*per_cent[banks[k]])
    k = k+1

    if k==i:
        break

print (deposit)

deposit.sort()
j=int(len(deposit))
print(deposit[j-1])


