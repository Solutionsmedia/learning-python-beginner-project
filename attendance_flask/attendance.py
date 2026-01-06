# Attendance.py
from errors import AttendanceError
from database import Database


class Attendance:

    @staticmethod
    def mark_attendance(data):
        db = Database()
        if db.append(data):
            return True

    @staticmethod
    def list_attendance():
        db = Database()
        attendance = db.read_db()
        return attendance
