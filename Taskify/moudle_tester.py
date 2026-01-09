from database import Database
from errors import DatabaseError
from task import Task
from authenticate import Auth
DATABASE_FILE = "task.json"
db = Database(DATABASE_FILE)
authenticate = Auth()


def test_init():
    db._system_file_check()
    print("Files Initilized succesfully")


def test_db_write():
    data = {"Data": "Test"}
    try:
        db.write_db(data)
        print("Data Written Succesfully")

    except Exception as e:
        print(e)


def test_task_update():
    data = {"title": "SEE Food",
            "status": "True"
            }
    try:
        update_task = Task()
        update_task.update_task_status(data)
        print("Task Changed Succesfully")

    except Exception as e:
        raise DatabaseError(f"{e}")


def test_title_update():
    prev_title = "Kill Food"
    data = {"title": "SEE Food",
            "status": "fire"
            }
    try:
        update_task = Task()
        update_task.update_task_title(prev_title, data)
        print("Task Title Changed Succesfully")
    except Exception as e:
        raise DatabaseError(f"{e}")

# ------- User Acount---------
# user_name
# password
# First_Name
# Last_Name


def test_create_user():
    data = {"user_name": "semiu",
            "password": "12345",
            "First_Name": "Oyinlola",
            "Last_Name": "Onatade"
            }
    authenticate.create_user(data)
    print("successful")


def test_login_user():
    data = {"user_name": "semiu",
            "password": "12345"
            }

    user_name = authenticate.login_user(data)
    print(f"Welcome {user_name}")


def main():
    # test_init()
    # test_db_write()
    # test_title_update()
    # test_task_update()
    test_create_user()
    test_login_user()
    print("All Test Successful")


if __name__ == "__main__":
    main()
