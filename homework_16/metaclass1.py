import datetime
import json
import requests

class ATM:
    def __init__(self, pin, balance):
        self._pin = pin
        self.balance = balance
        self._currency = 'USD'
        self._transactions = []

    def check_pin(self, pin):
        m = 3
        while m > 0:
            if pin == self._pin:
                print("PIN accepted.")
                return True
            else:
                m -= 1
                print(f'Wrong pin, {m} attempts left.')
                pin = input('Enter pin: ')
        print("Card is blocked.")
        return False

    def withdrawal_funds(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawal successful. Balance: {self.balance}')
            self._record_transaction("Withdrawal", amount)
        else:
            print('Insufficient funds.')

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f'Deposit successful. Balance: {self.balance}')
            self._record_transaction("Deposit", amount)
        else:
            print('Invalid deposit amount.')

    def exchange_rate(self, target):
        response = requests.get(f'https://v6.exchangerate-api.com/v6/a5ecc1a57123d3cd8896bc1d/latest/{self._currency}')
        data = response.json()
        rate = data['conversion_rates'].get(target)
        if rate:
            print(f'Exchange rate for {target}: {rate}')
        else:
            print(f'Invalid target currency: {target}')
        return rate

    def convert(self, amount, target):
        rate = self.exchange_rate(target)
        if rate:
            converted_amount = amount * rate
            print(f'Successful conversion. Amount in {target}: {converted_amount}')
            self._record_transaction("Currency Conversion", amount, target)

    def _record_transaction(self, operation_type, amount, currency=None):
        transaction_data = {
            "datetime": str(datetime.datetime.now()),
            "operation_type": operation_type,
            "amount": amount,
            "currency": currency
        }
        self._transactions.append(transaction_data)
        self._save_transactions()

    def _save_transactions(self):
        with open("transactions.log", "a") as file:
            json.dump(self._transactions[-1], file)
            file.write("\n")

# Example Usage:
user_ATM = ATM('1234', 1000)
pin_entered = input('Enter PIN: ')
if user_ATM.check_pin(pin_entered):
    user_ATM.convert(100, 'AFN')
    user_ATM.deposit(89)
    user_ATM.withdrawal_funds(100)
    user_ATM.exchange_rate('AFN')
