import json
import os
from errors import DatabaseError
DATABASE_FILE = "task.json"


class Database:
    def __init__(self, filename):
        self.filename = filename
        self._system_file_check()

    def _system_file_check(self):
        if not os.path.exists(self.filename):
            data = []
            with open(self.filename, "w") as f:
                json.dump(data, f)

    def load_db(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return data
        except Exception as e:
            raise DatabaseError(
                f"System level error occured while reading the Database, system says: {e}")

    def write_db(self, data):
        try:
            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            raise DatabaseError(
                f"System Level error occured while writing the database, system says: {e}")

    def update_db(self, data):

        try:
            db = self.load_db()
            db.append(data)
            self.write_db(db)
            return True
        except Exception as e:
            raise DatabaseError(
                f"A system Level Error Occured While updating and writing the db, system says: {e}")
