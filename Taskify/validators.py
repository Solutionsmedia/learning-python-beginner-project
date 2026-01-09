from errors import TaskError
# Task Fields
# title

# description

# status → pending / done

# date_created

# ------- User Acount---------
# user_name
# password
# First_Name
# Last_Name


class Validator():
    @staticmethod
    def validate_task(data):
        if not isinstance(data, dict):
            raise TaskError("Error processing data. Data may be corrupted")
        if "title" not in data:
            raise TaskError("Invalid Data format, Titile is not in data")
        if "title" == "":
            raise TaskError("Title cannot be empty")
        if not isinstance(data["title"], str):
            raise TaskError("Kindly Enter a valid title")
        if "description" not in data:
            raise TaskError("Invalid Data Format, Description is not in data")
        if "description" == "":
            raise TaskError("Description can not be empty")
        if not isinstance(data["description"], str):
            raise TaskError("Kidnly Enter a valid Description")
        status_data = ["pending", "done"]
        if "status" not in data:
            raise TaskError("Invalid Data Format, Status not in data")
        if "status" == "":
            raise TaskError("Task status can not be empty")
        if not isinstance(data["status"], str):
            raise TaskError("Invalid data format, Enter a valid status")
        if data["status"].strip().lower() not in status_data:
            raise TaskError("Enter a valid Task Status")
        return True

    @staticmethod
    def validate_user(data):
        if not isinstance(data, dict):
            raise TaskError("Error processing data. Data may be corrupted")
        if "user_name" not in data:
            raise TaskError("Invalid Data format, User Name is not in data")
        if "user_name" == "":
            raise TaskError("User Name cannot be empty")
        if not isinstance(data["user_name"], str):
            raise TaskError("Invalid Data Format, User_Name is Currupted")
        if "password" not in data:
            raise TaskError("Invalid Data Format, Password is not in data")
        if "password" == "":
            raise TaskError("Description can not be empty")
        if not isinstance(data["password"], str):
            raise TaskError("Invalid Data Format, Password is Currupted")
        if "First_Name" not in data:
            raise TaskError("Invalid Data Format, First Name is not in data")
        if "First_Name" == "":
            raise TaskError("Your First Name is required")
        if not isinstance(data["First_Name"], str):
            raise TaskError(
                "Invalid Data Format, First Name Data is Currupted")
        if "Last_Name" not in data:
            raise TaskError("Invalid Data Format, Last Name is not in data")
        if "Last_Name" == "":
            raise TaskError("Your Last Name is required")
        if not isinstance(data["Last_Name"], str):
            raise TaskError("Invalid Data Format, Last Name Data is Currupted")
        return True

    def validate_login(data):
        if not isinstance(data, dict):
            raise TaskError("Error processing data. Data may be corrupted")
        if "user_name" not in data:
            raise TaskError("Invalid Data format, User Name is not in data")
        if "user_name" == "":
            raise TaskError("User Name cannot be empty")
        if not isinstance(data["user_name"], str):
            raise TaskError("Invalid Data Format, User_Name is Currupted")
        if "password" not in data:
            raise TaskError("Invalid Data Format, Password is not in data")
        if "password" == "":
            raise TaskError("Description can not be empty")
        if not isinstance(data["password"], str):
            raise TaskError("Invalid Data Format, Password is Currupted")
        return True
