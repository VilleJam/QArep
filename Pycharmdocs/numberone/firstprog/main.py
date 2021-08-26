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


S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение суммы после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)