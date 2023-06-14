# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

CASH_WITHDRAWAL_FEE_MAX = 600
CASH_WITHDRAWAL_FEE_MIN = 30
PERCENT_WITHDRAW = 0.03
PERCENT_PREMIAL = 0.03
MULTIPLICITY_CASH = 50
balance = 0
count_operations = 0
run = True
records_operation = []


def add_cash(balance):
    print(f"Сумма пополнения кратны {MULTIPLICITY_CASH} у.е.")
    add_money = input("Внесите суму:")
    if add_money.isdigit() and int(add_money) % MULTIPLICITY_CASH == 0:
        balance += int(add_money)
        records_operation.append("Пополнение:" + add_money)
    else:
        print("Не корректная сумма")
    return balance


def withdraw_cash(balance):
    print(f"Сумма для снятия кратна {MULTIPLICITY_CASH} у.е. ")
    get_money = input("укажите  сумму которую хотите снять: ")
    if get_money.isdigit():
        get_money = int(get_money)
        if get_money > balance:
            print(
                f"Запрашиваемая сумма {get_money} y.e  больше суммы на Вашем счете {balance} y.e"
            )
        else:
            if get_money % MULTIPLICITY_CASH == 0:
                if get_money * PERCENT_WITHDRAW > CASH_WITHDRAWAL_FEE_MAX:
                    percent_cash = CASH_WITHDRAWAL_FEE_MAX
                elif get_money * PERCENT_WITHDRAW < CASH_WITHDRAWAL_FEE_MIN:
                    percent_cash = CASH_WITHDRAWAL_FEE_MIN
                else:
                    percent_cash = get_money * PERCENT_WITHDRAW
                    print(f"Коммисия за снятие наличных {percent_cash}")
                balance -= get_money + percent_cash
                records_operation.append(
                    "Снято:" + str(get_money) + " и коммисия:" + str(percent_cash)
                )
            else:
                print("Некорректная сумма")
    return balance


while run:
    print(
        """                 
                     Добро пожаловать В банк "Рога и Копыта"!!!
    Для выбора операции введите сответствующую цифру соответствующую операции
    1 - Пополнить счет
    2 - Снять наличные
    3 - Просмотреть все операции
    4 - Выйти
    """
    )
    choice = input("Выбор операции:")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1 or choice == 2:
            if balance >= 5_000_000:
                print(
                    f"С Вас удержан налог на богатство 10% в размере {balance * 0.10}"
                )
                records_operation.append(
                    "удержан налог на богатство:-" + str(balance * 0.10)
                )
                balance -= balance * 0.10
            if choice == 1:
                balance = add_cash(balance)
                count_operations += 1
            elif choice == 2:
                balance = withdraw_cash(balance)
                count_operations += 1
            else:
                print("Некорректный ввод")
        elif int(choice) == 3:
            print(records_operation)
        elif int(choice) == 4:
            run = False
    else:
        print("Некоректный выбор")
    if count_operations == 3:
        print(
            f"Вам начиcлены 3% в размере {balance * PERCENT_PREMIAL} у.е к счету за частое использование услуг нашего банка"
        )
        records_operation.append(
            "3%  за частое использование услуг:" + str((balance * PERCENT_PREMIAL))
        )
        balance += balance * PERCENT_PREMIAL
        count_operations = 0
    print(f"Баланс вашего счета составляет {balance}  у.е")
print("Сеанс работы закончен")
