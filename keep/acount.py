import streamlit as st
import json
import os
from datetime import datetime
DATABASE = "account.json"

# _______ VISION_________
# (Personal Finance)
# What it does(very useful in real life)
# A small app where you:
# add an expense(name + amount)
# see total money spent
# list all expenses
# handle errors properly(empty input, wrong numbers, etc.)
# This is way simpler than the library project but teaches the same core skills.

# _______Error Module_______


class AccountError(Exception):
    pass


# Initiating Database Backend Functions
class Database:
    def __init__(self, database):
        self.database = database
        self._check_db_health_()

    def _check_db_health_(self):
        try:
            if not os.path.exists(self.database):
                with open(self.database, 'w')as f:
                    data = []
                    json.dump(data, f)
        except Exception as e:
            raise AccountError(
                f"System Error Occured while checking the database files, system says: {e}")

# _________ READ FUNCTION TESTED____________

    def read(self):
        try:
            with open(self.database, "r") as f:
                data = json.load(f)
                return data
        except Exception as e:
            AccountError(
                f"System Error occured while reading the file, system says: {e}")

  # ____________ WRITE FUNCTION TESTED__________

    def write(self, data):
        try:
            with open(self.database, 'w') as f:
                json.dump(data, f, indent=4)
                return True
        except Exception as e:
            raise AccountError(
                f"A system errror occured while writing the data, system says: {e}")
# _________APPEND FUCNTION TESTED___________

    def append(self, data):
        db = self.read()
        db.append(data)
        self.write(db)
        return True

    def validate_data(self, data):
        if not isinstance(data, dict):
            raise AccountError("Invalid Data Structure")
        if "Transaction_type" not in data:
            raise AccountError("Transaction_Type Required")
        if not isinstance(data["Transaction_type"], str):
            raise AccountError("Transaction_Type Must be string")
        if data["Transaction_type"].strip() == "":
            raise AccountError("Transaction Type cannot be empty")
        if "Amount" not in data:
            raise AccountError("Amount is required.")
        if not isinstance(data['amount'], int):
            raise AccountError("Amount must be an integer.")
        if data["amount"] <= 0:
            raise AccountError("Amount Must be greater than 0")

        return True


class Finance:
    def __init__(self):
        self.database = Database

    def save_expense(self, data):
        if data["Transaction_type"] == "":
            raise AccountError("Transaction cannot  be empty")
        if data["Amount"] is not int:
            raise AccountError("Expense amount has to be figure")
        self.database.append(data)
        return True


def main():
    db = Database(DATABASE)
    fin = Finance()
    # Initializing State
    if "action" not in st.session_state:
        st.session_state.action = None
        st.rerun()
    if "view_expense" not in st.session_state:
        st.session_state.view_expense = None
        st.rerun()
    if st.session_state.action is None:
        st.title("Personal Expense Keeper")
        st.header("Add and view overview of your expenses here")
        st.subheader("What would you like to do??")
        if st.button("Add Expense", key="add_exp_btn"):
            st.session_state.action == "add_expense"
            st.rerun()

        if st.button("View Expense"):
            st.session_state.action == "view_expense"
            st.rerun()

        if st.session_state.action == "add_expense":
            exp_type = st.selectbox(
                "choose a transaction Type",
                ["Deposit", "Withrawal", "Transfer"]
            )
            exp_amount = st.number_input("How much is it?")
            data = {
                "Transaction_type": exp_type,
                "Amount": exp_amount,
                "Time": datetime.now().isoformat()
            }
            if st.button("save", key="add_save_btn"):
                try:
                    db.validate_data(data)
                except Exception as e:
                    st.error(e)
                st.session_state.add_expense = fin.save_expense(data)
                st.rerun()

        if st.button("View Expense"):
            pass


if __name__ == "__main__":
    main()
