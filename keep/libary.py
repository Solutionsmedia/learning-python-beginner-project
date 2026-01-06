
import json
import os
from datetime import datetime
import streamlit as st
DATABASE = "book.json"
LOGGER = "logger.txt"


class Database:
    def __init__(self, filename):
        self.file = filename
        self._db_check()

    def _db_check(self):
        if not os.path.exists(self.file):
            data = []
            with open(self.file, 'w') as f:
                json.dump(data, f, indent=4)

    def write(self, data):
        try:
            with open(self.file, 'w') as f:
                json.dump(data, f, indent=4)
                return True
        except Exception as e:
            raise LibraryError(f"Failed to write database: {e}")

    def read(self):
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
                return data
        except Exception as e:
            raise LibraryError(f"Error Reading Database: {e}")

    def update(self, data):
        db = self.read()
        for book in db:
            if book["title"] == data["title"]:
                raise LibraryError(f"{book['title']} exists in the library")

        db.append(data)
        self.write(db)
        return True


class LibraryError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self._log_error()

    def _log_error(self):
        try:
            if not os.path.exists(LOGGER):
                timestamp = datetime.now().isoformat()
                message = "Log Initialization Complete"
                with open(LOGGER, 'w') as f:
                    data = f"{timestamp}  : {message} \n"
                    f.write(data)
            else:
                timestamp = datetime.now().isoformat()
                with open(LOGGER, 'a') as f:
                    data = f"{timestamp}  : {self} \n"
                    f.write(data)
        except Exception as e:
            return f"System error occured, system says: {e}"


class Library:
    def __init__(self, data):
        self.db = Database(DATABASE)

    def add_book(self, data):
        self.db.update(data)
        return True

    def list_book(self):
        books = self.db.read()
        if not books:
            raise LibraryError("No existing book in the library")
        return books

    def borrow_book(self, title):
        library = self.db.read()
        for book in library:
            if book["title"] == title:
                if book["copies"] > 0:
                    book['copies'] -= 1
                    self.db.write(library)
                    return book["copies"]
                else:
                    return f"No avaliable copies for {title}"

        return f"This book does not exist in the library"

    def return_book(self, title):
        library = self.db.read()
        for book in library:
            if book["title"] == title:
                book['copies'] += 1
                self.db.write(library)
                return book["copies"]

        raise LibraryError("This book does not exist in the library")


def main():
    st.title("The Web Library")

    # ---- STATE SETUP ----
    if "role" not in st.session_state:
        st.session_state.role = None

    if "borrow_result" not in st.session_state:
        st.session_state.borrow_result = None

    if "need" not in st.session_state:
        st.session_state.need = None

    if "book_data" not in st.session_state:
        st.session_state.book_data = None

    if "status" not in st.session_state:
        st.session_state.status = None

    lib = Library(Database)

    # ---- ROLE SELECTION ----
    if st.session_state.role is None:
        st.header("Welcome to the international Library")
        st.write("Choose an account type")

        if st.button("Student"):
            st.session_state.role = "student"
            st.rerun()

        if st.button("Librarian"):
            st.session_state.role = "librarian"
            st.rerun()

    # ---- STUDENT PAGE ----
    if st.session_state.role == "student":
        st.header("Student Library 📚")

        book_name = st.text_input("What book do you want to borrow?")

        if st.button("Search / Borrow"):
            st.session_state.borrow_result = lib.borrow_book(book_name)
            st.rerun()

        # ---- RESULT DISPLAY ----
        if st.session_state.borrow_result is not None:
            result = st.session_state.borrow_result

            if isinstance(result, int):
                st.success(
                    f"Book borrowed successfully. Copies left: {result}")
            else:
                st.error(result)

        if st.button("Back"):
            st.session_state.role = None
            st.session_state.borrow_result = None
            st.rerun()

   # _ _ _ _ LIBRARIAN PAGE _ _ _ _
    if st.session_state.role == "librarian":
        st.header("Librarian Dashboard")
        st.write("What would you love to do today?")

        if st.button("Add Book"):
            st.session_state.need = "add_book"
            st.session_state.status = None
            st.rerun()

        if st.button("List Books"):
            st.session_state.need = "list_book"
            st.rerun()

        if st.session_state.need == "add_book":
            add_book_name = st.text_input(
                "Kindly Enter the name of the book you want to add"
            ).strip()
            add_book_author = st.text_input(
                "What is the author's name?").strip()
            add_book_copies = st.number_input(
                "How Many Copies?", min_value=1, step=1
            )

            if st.button("Save"):
                st.session_state.status = None
                try:
                    book_data = {
                        "title": add_book_name,
                        "author": add_book_author,
                        "copies": add_book_copies,
                    }
                    lib.add_book(book_data)
                    st.session_state.status = "success"   # ✅ ONLY here
                except LibraryError as e:
                    st.session_state.status = str(
                        e)      # ✅ STORE ERROR MESSAGE
                st.rerun()

            # ---- FEEDBACK ----
            if st.session_state.status == "success":
                st.success("Book Added Successfully")
            elif st.session_state.status is not None:
                st.error(st.session_state.status)
            if st.button("Back"):
                st.session_state.need = None
                st.rerun()

        if st.session_state.need == "list_book":
            try:
                books = lib.list_book()
                st.subheader("Available Books")
                st.table(books)
            except LibraryError as e:
                st.error(str(e))
            if st.button("Back"):
                st.session_state.need = None
                st.rerun()


if __name__ == "__main__":
    main()
