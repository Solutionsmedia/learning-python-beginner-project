import os
import json


class Database:
    def __init__(self, filename):
        self.filename = filename
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def read(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

    def write(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def append(self, item):
        data = self.read()
        data.append(item)
        self.write(data)


class User:
    def __init__(self, name, role, balance=0):
        self.name = name
        self.role = role
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} deposit ${amount}. New balance: ${self.balance}")
        else:
            print("Enter a valid amount")
    
    def get_balance(self):
        return self.balance
    
    def get_role(self):
        

