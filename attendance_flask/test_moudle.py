# test_moudle.py
from database import Database
from errors import AttendanceError, DatabaseError
from attendance import Attendance

db = Database()

data = {
    "student_name": "John Doe",
    "date": "2026-01-05",
    "status": "present"}


def test_db_function():
    # Testing Reading (Successful)
    data = db.read_db()
    print(data)

    # Testing Appending and writing (Successful)
    data = {
        "student_name": "John Dim",
        "date": "2026-01-05",
        "status": "present"
    }
    try:
        if db.append(data):
            print("Successfully Write DB")
    except Exception as e:
        raise AttendanceError(
            f"An error occured while processing your request: {e}")


def main():
    print(Attendance.mark_attendance(data))


if __name__ == "__main__":
    main()
