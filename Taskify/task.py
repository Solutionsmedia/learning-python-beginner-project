from errors import TaskError
from database import Database
from validators import Validator
DATABASE_FILE = "task.json"


class Task:
    def __init__(self):
        self.db = Database(DATABASE_FILE)
        self.validate = Validator()

    def add_task(self, data):
        self.validate.validate_task(data)
        self.check_duplicate(data)
        self.db.update_db(data)
        return True

    def list_task(self):
        task = self.db.load_db()
        return task

    def update_task_status(self, task):
        db = self.db.load_db()
        try:
            updated = False
            for entry in db:
                if entry.get("title") == task["title"]:
                    entry['status'] = task["status"]
                    updated = True
                    break
            if updated:
                self.db.write_db(db)
                return True
            else:
                raise TaskError("No task with such title")

        except Exception as e:
            raise TaskError(f"{e}")

    def update_task_title(self, prev_title, task):
        db = self.db.load_db()
        try:
            updated = False
            for entry in db:
                if entry.get("title") == prev_title:
                    entry["title"] = task["title"]
                    updated = True
                    break
            if not updated:
                raise TaskError("Title Not found")
            self.db.write_db(db)
            return True
        except Exception as e:
            raise TaskError(f"{e}")

    def check_duplicate(self, data):
        db = self.db.load_db()
        if "title" not in db:
            raise TaskError(
                "System Level Error Occured, cant find title key")
        for task in db:
            if data["title"] == task["title"]:
                raise TaskError("This Task Exists already")
