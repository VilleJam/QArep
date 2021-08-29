print("Введите количество необходимых билетов:")
tickets = int(input())

ticket_list = [i for i in range (1,tickets+1)]
print(ticket_list)

age_list = [int(input()) for i in range (tickets)]
print(age_list)

price = 0

for a, b in zip(ticket_list,age_list):
    if 0<b<18:
        price +=0
    elif 18<=b<=25:
        price += 990
    elif 25<b:
        price += 1390
    ticket = a
    age = b
    print(f"Билет {ticket}, возраст посетителя {age} ")

if tickets>3:
    print(f"Вы покупаете больше трех билетов, вам предоставляется скидка 10%. Цена за билеты {price*0.9}")
else:
    print(f"Вы покупаете билеты в количестве {tickets} штук, сумма покупки: {price}")
