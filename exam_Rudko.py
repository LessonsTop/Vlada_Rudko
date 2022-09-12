import json
from MegaClass import Account
from db import *


def main():
    # listNames = ["Valera", "Artem", "Kolya", "Petya", "Kostya"]
    # listNumbers = ["+7-903-800-00-00", "+7-908-222-80-00", "+79000002121", "89003211234", "89077077070"]
    # listEmail = ["test@test.ru", "artem@gmail.com", "kolya@mail.ru", "petya@yandex.ru", "kostya@rambler.ru"]
    # listBalance = [1000, 3450, 980, 1250, 398]
    sqlConnect.connect()
    sqlConnect.create_tables([AccountDb])

    account1 = Account('Valera', '+7-900-000-00-00', 'valera@mail.com', 100)
    users = AccountDb.create(account=account1.accountName, phone=str(account1.phone), email=account1.email, balance=account1.balance)
    # users.save()
    users = users.select()
    # for records in users.tuples().iterator():
    #     print(records)
    #     for v in records:
    #         print(v)

    val = AccountDb.delete().where(AccountDb.account == "Valera")
    val.execute()

    account1 = Account('Valera', '+7-903-800-00-00', 'test@test.ru', 1000)
    user1 = AccountDb.create(account=account1.accountName, phone=str(account1.phone), email=account1.email, balance=account1.balance)
    account2 = Account('Artem', '+7-908-222-80-00', 'artem@gmail.com', 3450)
    user2 = AccountDb.create(account=account2.accountName, phone=str(account2.phone), email=account2.email, balance=account2.balance)
    account3 = Account('Kolya', '+79000002121', 'kolya@mail.ru', 980)
    user3 = AccountDb.create(account=account3.accountName, phone=str(account3.phone), email=account3.email, balance=account3.balance)
    account4 = Account('Petya', '+89003211234', 'petya@yandex.ru', 1250)
    user4 = AccountDb.create(account=account4.accountName, phone=str(account4.phone), email=account4.email, balance=account4.balance)
    account5 = Account('Kostya', '89077077070', 'kostya@rambler.ru', 398)
    user5 = AccountDb.create(account=account5.accountName, phone=str(account5.phone), email=account5.email, balance=account5.balance)
    """можно исправить разный формат написания телефонов"""
    listAccounts = [account1, account2, account3, account4, account5]
    users = AccountDb.select()
    listAccount = []

    for records in listAccounts:
        listAccount.append(records.__dict__)
    accountJson = json.dumps(listAccount, indent=4)
    print(accountJson)


    with open("account.json", "w") as file:
        file.write(accountJson)


if __name__ == '__main__':
    main()