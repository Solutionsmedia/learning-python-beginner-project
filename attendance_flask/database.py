# Database.py
import json
import os
from errors import DatabaseError, AttendanceError
from validators import Validate
from datetime import datetime
DATABASE_FILE = "attendance.json"
# Database Strucure
# {
#     "student_name": "John Doe",
#     "date": "2026-01-05",
#     "status": "present"
# }


class Database:
    def __init__(self):
        filename = DATABASE_FILE
        self.filename = filename
        self._check_db_status()

    def _check_db_status(self):
        if not os.path.exists(self.filename):
            data = []
            with open(self.filename, "w") as f:
                json.dump(data, f)

    def read_db(self):
        with open(self.filename, "r") as f:
            data = json.load(f)
            return data

    def append(self, data):
        try:
            validator = Validate(data)
            if validator.validate():
                if self.chek_duplicate(data):
                    db = self.read_db()
                    db.append(data)
                    self.write_db(db)
                    return True
        except Exception as e:
            raise DatabaseError(
                f"System level error occured while appending and writing the information, system says {e}")

    def write_db(self, data):
        try:
            with open(self.filename, 'w')as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            raise DatabaseError(
                f"A system Level Error Occured while writing the databse, system says {e}")

    def chek_duplicate(self, data):
        db = self.read_db()
        for entry in db:
            if entry['student_name'].strip().lower() == data['student_name'].strip().lower():
                if data['date'] == entry['date']:
                    raise AttendanceError("You have marked your attendance.")
        return True
