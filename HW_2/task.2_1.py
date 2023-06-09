balance = 0
count_operations = 0
run = True
while run:

    print('''                 
                     Добро пожаловать В банк "Рога и Копыта"!!!
    Для выбора операции введите сответствующую цифру соответствующую операции
    1 - Пополнить счет
    2 - Снять наличные
    3 - Выйти
    ''')
    choice = input("Выбор операции:")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1 or choice == 2:
            if balance >= 5_000_000:
                print(
                    f'С Вас удержан налог на богатство 10% в размере {balance * 0.10}')
                balance -= balance * 0.10
            if choice == 1:
                print('Сумма пополнения кратны 50 у.е.')
                add_money = input('Внесите суму:')
                if add_money.isdigit() and int(add_money) % 50 == 0:
                    balance += int(add_money)
                    count_operations += 1
                else:
                    print('Не корректная сумма')
            elif choice == 2:
                print('Сумма для снятия кратна 50 у.е. ')
                get_money = input('укажите  сумму которую хотите снять: ')
                if get_money.isdigit():
                    get_money = int(get_money)
                    if get_money > balance:
                        print(
                            f"Запрашиваемая сумма {get_money} y.e  больше суммы на Вашем счете {balance} y.e")
                    else:
                        if get_money % 50 == 0:
                            if get_money * 0.03 > 600:
                                percent_cash = 600
                            elif get_money * 0.03 < 30:
                                percent_cash = 30
                            else:
                                percent_cash = get_money * 0.03
                            print(
                                f'Коммисия за снятие наличных {percent_cash}')
                            balance -= get_money + percent_cash
                            count_operations += 1
                        else:
                            print('Некорректная сумма')
                else:
                    print('Некорректный ввод')
        elif int(choice) == 3:
            run = False
    else:
        print('Некоректный выбор')
    if count_operations == 3:
        print(
            f"Вам начиcлены 3% в размере {balance*0.03} у.е к счету за частое использование услуг нашего банка")
        balance += balance * 0.03
        count_operations = 0
    print(f"Баланс вашего счета составляет {balance}  у.е")
print("Сеанс работы закончен")
