price = 0
while True:
    try:
        tickets = input('Введите количество билетов: ')
        tickets = int(tickets)
        if type(tickets) == int:
            break
    except ValueError:
        print('Введены некорректные данные! Пожалуйста, введите целое число.')
for i in range(tickets):
    i += 1
    while True:
        try:
            tickets_age = input(f'Укажите возраст посетителя для билета №{i}: ')
            tickets_age = int(tickets_age)
            if tickets_age < 18:
                print('Билет бесплатный')
            elif 25 > tickets_age >= 18:
                price += 990
                print('Стоимость билета: 990 руб.')
            else:
                price += 1390
                print('Стоимость билета: 1390 руб.')
            if type(tickets_age) == int:
                break
        except ValueError:
            print('Введены некорректные данные! Пожалуйста, введите целое число.')
if tickets > 3:
    price = price - ((price / 100) * 10)
    print(f'Сумма к оплате {price} руб. с учетом скидки')
else:
    print(f'Сумма к оплате {price} руб.')