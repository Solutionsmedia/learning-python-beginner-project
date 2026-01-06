# Validators.py
from errors import DatabaseError


# {
#     "student_name": "John Doe",
#     "date": "2026-01-05",
#     "status": "present"
# }

class Validate:
    def __init__(self, data):
        self.data = data

    def validate(self):
        if not isinstance(self.data, dict):
            raise DatabaseError("Data entry not allowed due to corrupt values")
        if "student_name" not in self.data:
            raise DatabaseError(
                "Incorrect Data, Student name dosent exist  in data")
        if "date" not in self.data:
            raise DatabaseError("Date dosent exist in data")
        if "status" not in self.data:
            raise DatabaseError("Student Status dosent exist in data")
        if self.data['student_name'] == "":
            raise DatabaseError("Student Name cannot be empty")
        if not isinstance(self.data['student_name'], str):
            raise DatabaseError("Invalid name format")
        if self.data['status'] == "":
            raise DatabaseError("Attendance Status Cannot be Empty ")
        if not isinstance(self.data['status'], str):
            raise DatabaseError("Invalid Status Format")
        if self.data['date'] == "":
            raise DatabaseError("Datec field cannot be empty")
        if not isinstance(self.data['date'], str):
            raise DatabaseError("Date format entry is corrupted")
        return True
