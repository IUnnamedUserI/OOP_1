#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Реализовать класс Account, представляющий собой банковский счет. В классе
должны быть четыре поля: фамилия владельца, номер счета, процент начисления
и сумма в рублях. Открытие нового счета выполняется операцией инициализации.
Необходимо выполнять следующие операции: сменить владельца счета, снять
некоторую сумму денег со счета, положить деньги на счет, начислить проценты,
перевести сумму в доллары, перевести сумму в евро, получить
сумму прописью (преобразовать в числительное).
'''


class Account:

    def __init__(self, surname, number, percent, cash):
        'Метод инициализации необходимых атрибутов класса'

        self.surname = str(surname)
        self.number = str(number)
        self.percent = float(percent)
        self.cash = float(cash)

    def change_owner(self, newOwner):
        'Метод смены владельца счёта'

        self.surname = newOwner

    def display(self):
        'Метод вывода информации о созданном счёте'

        print(f"{self.surname} | {self.number} | {self.percent} |",
              f"{self.cash}")


class AccountManagement:

    def withdraw_money(self, money, account: Account):
        'Метод для снятия денежных средств со счёта аккаунта'

        if account.cash >= int(money):
            account.cash -= int(money)
        else:
            print("На счету недостаточная сумма для выполнения операции")

    def put_money(self, money, account: Account):
        'Метод пополнения денежных средств на аккаунте'

        account.cash += int(money)


class InterestHandler:

    def __init__(self, account: Account):
        'Метод инициализации'

        self.percent = account.percent

    def accrue_percent(self, account: Account):
        account.cash += account.cash * self.percent / 100


class Converter:

    def transfer_dollar(self, account: Account):
        'Метод перевода валюты на счёте аккаунта в доллары'

        print(f"Перевод в доллары: ${round(account.cash / 90, 2)}")

    def transfer_euro(self, account: Account):
        'Метод перевода валюты на счёте аккаунта в евро'

        print(f"Перевод в евро: €{round(account.cash / 100, 2)}")

    def transfer_text(self, account: Account):
        'Метод перевода валюты в текстовый формат'

        text_number = round(account.cash)
        result = ""
        if text_number > 10000:
            print(f"Сумма больше 10.000 ({account.cash})")
            return
        else:
            units = ["", "один", "два", "три", "четыре", "пять", "шесть",
                     "семь", "восемь", "девять"]
            teens = ["", "десять", "одинадцать", "двенадцать", "тринадцать",
                     "четырнадцать", "пятнадцать", "шестнадцать",
                     "семнадцать", "восемнадцать", "девятнадцать"]
            tens = ["", "десять", "двадцать", "тридцать", "сорок",
                    "пятьдесят", "шестьдесят", "семьдесят", "восемьдесять",
                    "девяносто"]
            hunders = ["", "сто", "двести", "триста", "четыреста", "пятьсот",
                       "шестьсот", "семьсот", "восемьсот", "десятьсот"]

            if text_number >= 1000:
                thousand = text_number // 1000
                if thousand == 1:
                    result += "одна тысяча "
                elif thousand == 2:
                    result += "две тысячи "
                elif thousand == 3 or thousand == 4:
                    result += f"{units[thousand]} тысячи"
                else:
                    result += f"{units[thousand]} тысяч"

                text_number -= thousand * 1000

            if text_number >= 100 and text_number <= 999:
                hunder = text_number // 100
                result += f" {hunders[hunder]}"

                text_number -= hunder * 100

            if text_number >= 10 and text_number <= 19:
                result += f" {teens[text_number - 11]}"
            elif text_number >= 20 and text_number <= 99:
                ten = text_number // 10
                result += f" {tens[ten]}"
                text_number -= ten * 10

            if text_number > 0 and text_number <= 9:
                result += f" {units[text_number]}"

            if text_number == 0 or (text_number >= 5 and text_number <= 9):
                result += " рублей"
            elif text_number == 1:
                result += " рубль"
            elif text_number >= 2 and text_number <= 4:
                result += " рубля"

        print(f"Сумма прописью: {result} (₽{account.cash})")


if __name__ == "__main__":
    'Метод инициализации'

    account = Account("Иванов", "333-123", 20, 10000)
    account.display()
    account.change_owner("Петров")
    account.display()

    account_manager = AccountManagement()
    account_manager.withdraw_money(5000, account)
    account.display()
    account_manager.put_money(557, account)
    account.display()

    interest = InterestHandler(account)
    interest.accrue_percent(account)
    account.display()

    converter = Converter()
    converter.transfer_dollar(account)
    converter.transfer_euro(account)
    converter.transfer_text(account)
