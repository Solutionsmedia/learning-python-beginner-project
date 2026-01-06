import json
import os
from datetime import datetime, date, time
DATABASE_FILE = "db.json"
USER_DB = "gameuser.json"
admin_code = 234


def write_transaactions(log):
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as f:
            db = json.load(f)

        db.append(log)

        with open(DATABASE_FILE, "w")as f:
            json.dump(db, f, indent=4)
            return True
    else:
        print("Transactions Database is not initialized, ensure you called the initialization fuction or ensure the initiablzation suceeded.")


def write_user(name, password, permission):
    try:
        if os.path.exists(USER_DB):
            with open(USER_DB, "r") as f:
                db = json.load(f)
                data = {
                    "Name": name,
                    "password": password,
                    "status": permission
                }
                db.append(data)
                with open(USER_DB, "w") as f:
                    json.dump(db, f, indent=4)
                    return True
    except Exception as e:
        print(f"An Error occured, System says {e}")


def read(file):
    try:
        if os.path.exists(file):
            with open(file, "r") as f:
                data = json.load(f)
                return data
        else:
            data = []
            return data

    except Exception as e:
        print(f"An error occured, system says {e}")


def init_db():
    if not os.path.exists(DATABASE_FILE):
        data = []
        with open(DATABASE_FILE, "w")as file:
            json.dump(data, file)
            print("LOG Database initialization Complete")

    if not os.path.exists(USER_DB):
        data = []
        with open(USER_DB, "w")as file:
            json.dump(data, file)
            print("USER Database initialization Complete")


def select_user(user):
    if user == 1:
        return "user"
    elif user == admin_code:
        return "admin"
    else:
        return False


def deposit():
    while True:
        amount = input("How much do you want to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                data = {"transaction": "Deposit",
                        "amount": amount,
                        "time": datetime.now().isoformat()
                        }
                if write_transaactions(data):
                    print("Account Funded Succesfully")
                break
            else:
                print("Kindly enter a valid amount")
        else:
            print("Kindly Enter a valid digit between 1$ to ...... ")
            continue
    return amount


def admin_flow():
    if not read(USER_DB):
        print(
            "No admin found for this system, Admin Onboarding in progress, Stand By.....")
        admin_name = input(
            "Kindly Enter your a name to access your account: ")
        password = input(
            "Kindly Enter a password to acess your Account: ")
        permission = "admin"
        if write_user(admin_name, password, permission):
            print(
                "You account has beem created successfully, You can now login")

    else:
        while True:
            print("welcome Admin, Kindly Login.")
            admin_name = input("Kindly Enter your Username: ")
            password = input("kindly Enter your password: ")
            user = get_role(admin_name, password)
            if not user:
                print("invalid Username or password")
            else:
                role = user[1]
                print(f"Welcome {user[0]}")
                balance = admin_balance(role)
                if not balance:
                    print("You are not allowed to access this resource")
                else:
                    balance = admin_balance(role)
                print(f"Balance: ${balance}")
                transactions = read(DATABASE_FILE)
                print(transactions[-1])
                return


def user_flow():
    deposit()


def admin_balance(role):
    if role == "admin":
        transactions = read(DATABASE_FILE)
        total = 0
        for tx in transactions:
            total += tx["amount"]

        return total
    else:
        return None


def get_role(admin_name, password):
    db = read(USER_DB)
    for user in db:
        if user.get('Name') == admin_name and user.get('password') == password:
            role = user.get('status')

            return admin_name, role


def main():
    init_db()

    while True:
        print("Welcome To National Gaming Centre")
        try:
            user = int(
                input(f"Verifying you are human Kindly Enter this recapcha digit '1': "))
        except ValueError:
            print("Kindly Enter a valid digit")
            continue
        role = select_user(user)
        if role == "user":
            user_flow()

            continue
        elif role == "admin":
            admin_flow()
            continue
        else:
            print("Kindly Enter the right Recapcha text you can see on your screen")
            continue


if __name__ == "__main__":
    main()
