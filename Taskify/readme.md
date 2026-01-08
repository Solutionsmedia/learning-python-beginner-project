📝 Taskify — Student Task Tracker
A simple, clean task-tracking web app built with Flask to help students manage tasks and practice backend fundamentals.

🎯 Project Overview
Taskify is a lightweight task tracker where users can:

Add new tasks

View all tasks in a table

Mark tasks as completed

This project focuses on backend logic, data validation, and Flask fundamentals, while keeping the UI minimal and friendly.

It is intentionally simpler than an attendance system but uses the same core concepts, so everything finally clicks.

🧠 Why This Project Exists
This project helps reinforce:

Flask routing (GET & POST)

Form handling with request.form

Backend validation (never trust the frontend)

Error handling with try / except

JSON-based data storage

Rendering dynamic tables with Jinja

If you understand this project, you understand Flask basics properly.

🎨 Design Theme
Vibe: Clean • Calm • Focused • Student-friendly

Color Palette
--primary: #4F46E5;      /* Indigo */
--primary-hover: #4338CA;

--accent: #22C55E;       /* Success green */
--danger: #EF4444;       /* Error red */

--bg-main: #F8FAFC;      /* Light background */
--bg-card: #FFFFFF;

--text-main: #0F172A;
--text-muted: #64748B;
🧱 Features
Core Features
➕ Add a task

📋 View all tasks

✅ Mark task as completed

🕒 Auto-generate creation date

Task Fields
title

description

status → pending / done

date_created

🧭 Pages & Routes
Route	Method	Description
/	GET	View all tasks (table)
/add-task	GET, POST	Add a new task
/complete/<id>	POST	Mark task as done
🛠 Tech Stack
Python

Flask

Jinja2

HTML + CSS

JSON (file-based storage)

🗂 Suggested Project Structure
taskify/
│
├── main.py
├── tasks.json
│
├── templates/
│   ├── index.html
│   └── add_task.html
│
├── static/
│   └── style.css
│
├── validators.py
├── database.py
├── task.py
└── errors.py
⚠️ Same structure style as your attendance app — on purpose.

🔐 Validation Philosophy
Frontend helps the user

Backend protects the system

All data is validated before storage

Errors are raised in backend logic

Flask catches errors and shows friendly messages

You already learned this — now you’re applying it cleanly.

🚀 Learning Outcomes
After completing Taskify, you will confidently understand:

How Flask connects frontend ↔ backend

How to safely process form data

How to display backend data in HTML tables

How to structure small backend projects properly

How real apps actually work

💬 Final Note
This project is not about complexity.
It’s about clarity.

If Attendance felt like a mountain,
Taskify is the solid ground that makes you stable.