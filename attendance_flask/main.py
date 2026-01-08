from flask import Flask, render_template, request
from attendance import Attendance
from datetime import datetime
from errors import DatabaseError, AttendanceError
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/view-attendance")
def view_attendance():
    attendance = Attendance()
    attend_data = attendance.list_attendance()

    return render_template(
        "view_attendance.html",
        attend_data=attend_data
    )



@app.route("/attendance", methods=["GET", "POST"])
def attendance():
    if request.method == "POST":
        try:
            name = request.form.get("student_name", "").strip()
            status = request.form.get("status", "").strip()

            data = {
                "student_name": name,
                "date": datetime.now().date().isoformat(),
                "status": status
            }

            attendance = Attendance()
            attendance.mark_attendance(data)

            return render_template(
                "attendance_form.html",
                success="Attendance recorded successfully ✅"
            )

        except DatabaseError as e:
            return render_template(
                "attendance_form.html",
                error=str(e)
            )

        except AttendanceError as e:
            return render_template(
                "attendance_form.html",
                error=str(e)
            )

        except Exception:
            return render_template(
                "attendance_form.html",
                error="Something went wrong. Please try again."
            )

    return render_template("attendance_form.html")


if __name__ == "__main__":
    app.run(debug=True)
