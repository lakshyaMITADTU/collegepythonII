# Bank system with timestamp
import time

class Account:
    def __init__(self, holder, acc):
        self.holder = holder
        self.acc = acc
        self.money = 500

    def info(self):
        print(f"Holder: {self.holder} | Balance: ₹{self.money}")

    def add_money(self, amt):
        self.money += amt
        self.receipt("CREDIT", amt)

    def take_money(self, amt):
        if amt <= self.money:
            self.money -= amt
            self.receipt("DEBIT", amt)
        else:
            print("Low balance!")

    def receipt(self, typ, amt):
        print("\n--- TRANSACTION ---")
        print("Type:", typ)
        print("Amount:", amt)
        print("Balance:", self.money)
        print("Time:", time.ctime())
        print("-------------------\n")


user = Account(input("Name: "), input("Acc No: "))

while True:
    ch = input("\n1.Check 2.Deposit 3.Withdraw 4.Exit\nChoice: ")

    if ch == "1":
        user.info()
    elif ch == "2":
        user.add_money(float(input("Amount: ")))
    elif ch == "3":
        user.take_money(float(input("Amount: ")))
    elif ch == "4":
        break
