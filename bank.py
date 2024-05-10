# Определите класс "Account", имитирующий банковский счет.
# Класс должен включать атрибуты для хранения идентификации владельца,  баланс счета и
# методы для депозита (пополнения счета)  и  снятия средств,  если на счету  достаточно средств

class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет на {money}. Сумма  на счете  - {self.balance} рублей")

    def withdraw(self, money):
        if money >= self.balance:
            print(f"Недостаточно средств на счету, у вас - {self.balance} рублей")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money}. Сумма на счете  - {self.balance} рублей")

    def all_balance(self):
        print(f"Ваш текущий баланс - {self.balance} рублей")

man = Account(123432343, 600)

man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)