from errors import DatabaseError
from database import Database
from validators import Validator
USERS_FILE = "users.json"
# ------- User Acount---------
# user_name
# password
# First_Name
# Last_Name


class Auth:
    def __init__(self):
        self.db = Database(USERS_FILE)

    def login_user(self, data):
        users = self.db.load_db()
        Validator.validate_login(data)
        for entry in users:
            if data["user_name"] == entry["user_name"]:
                if data["password"] == entry["password"]:
                    return entry["First_Name"]
                raise DatabaseError("Invalid Password")
            raise DatabaseError("No User with such Name")

    def create_user(self, data):
        Validator.validate_user(data)
        self.db.update_db(data)
        return True
