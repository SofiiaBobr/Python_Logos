import datetime
import json
import requests
class ATM:
    def __init__(self, pin, balance):
        self._pin = pin
        self.balance = balance
        self._currency = 'USD'

    def check_pin(self, pin):
        m = 3
        while m > 0:
            if pin == self._pin:
                return True
            else:
                m-= 1
                print(f'Wrong pin, left {m} trys ')
                pin = input('Enter pin')
        return False

    def withdrawal_funds(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'On your balance {self.balance} left')
        else:
            print('No money')

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f'On your balance {self.balance} left')
        else:
            print('Wrong amount')

    def exchange_rate(self, target):
        respons = requests.get(f'https://v6.exchangerate-api.com/v6/a5ecc1a57123d3cd8896bc1d/latest/{self._currency}')
        data = respons.json()
        print(target,  data['conversion_rates'].get(target))
        return data['conversion_rates'].get(target)

    def convert(self, amount, target):
        rate = self.exchange_rate(target)
        if rate:
            print(f'Successfull operation {amount * rate}')

    def


user_ATM = ATM('1234', 1000)
user_ATM.convert(100, 'AFN')
user_ATM.deposit(89)
user_ATM.withdrawal_funds(100)
user_ATM.exchange_rate('AFN')
print(user_ATM.check_pin(input('Enter pin')))


