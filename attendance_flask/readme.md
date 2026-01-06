🎯 WHAT THE PROJECT DOES

A simple system that:

Records student attendance

Prevents duplicate attendance for the same day

Stores data in a JSON file

Validates all inputs

Uses clean structure and errors

📦 HIGH-LEVEL RULES (READ CAREFULLY)

You must:

Use Python only

Use JSON file as database

Use classes

Use custom exceptions

Separate logic from storage

Validate data before saving

📁 FILE STRUCTURE (ONLY THIS)

Create a folder:

attendance/
│
├── main.py
├── storage.py
├── validators.py
├── errors.py
└── attendance.json


👉 Do NOT ask what goes where yet.
Just create the files.

🧩 CORE DATA FORMAT (VERY IMPORTANT)

Each attendance record MUST look like this:

{
    "student_name": "John Doe",
    "date": "2026-01-05",
    "status": "present"
}


Rules:

student_name → string, not empty

date → YYYY-MM-DD (string)

status → either "present" or "absent"

🚫 STRICT RULES (THIS IS WHERE YOU THINK)
❌ These must be rejected:

Empty student name

Status not present/absent

Duplicate attendance (same student + same date)

Data that is not a dictionary

✅ These must pass:

Same student, different date

Different student, same date

🧪 REQUIRED FEATURES

Your program MUST support:

1️⃣ Add attendance
2️⃣ List all attendance
3️⃣ Show errors clearly (no silent failures)

CLI only (print statements are fine).

🛑 WHAT I WANT FROM YOU NOW (IMPORTANT)

DO NOT ASK ME FOR CODE.

Your task:

Create the folder & files

Decide:

What goes into errors.py

What goes into validators.py

What goes into storage.py

Write your first version of:

Adding attendance

Saving to JSON

It can be ugly.
It can be wrong.
It SHOULD be wrong.