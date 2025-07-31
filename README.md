# 👋 Hi, I'm Arun Kumar K

## 🛠️ My Projects
1. 🔥 Expense Tracker – Features
- 🔹 [Expense Tracker API](https://github.com/Arunkumar2504/expense_project)
- 🔹 [Live Link] https://expense-tracker-lwkb.onrender.com/

💡 Overview

This is a full-stack Expense Tracker built with Django and Django REST Framework, featuring a modern UI with Tailwind CSS and tools like Chart.js and DataTables.

✅ Key Features
🌐 Web Interface (Django + Tailwind CSS)
 - Add, Edit, Delete Expenses
  
 - View all expenses in a searchable, paginated table
  
 - Export table as CSV or Excel
  
 - Filter expenses by custom date range using Flatpickr
  
 - View charts of expenses over time (Chart.js)
  
 - Responsive mobile-first design

⚙️ Backend Functionality (DRF API – Optional)
Django REST API for expenses is available (can be reused or expanded)
  
  Pagination and date filtering supported in backend logic

🛠 Tech Stack

Backend: Python, Django, Django REST Framework

  Frontend: HTML, Tailwind CSS, JavaScript
  
  Plugins: Chart.js, DataTables.js, Flatpickr.js
  
  Database: SQLite (easy to switch to MySQL or PostgreSQL)

📌 Future Roadmap
  These are some features and improvements planned for upcoming versions:
  
  ✅ User Authentication System
  Allow multiple users to manage their own expenses with login/register/logout functionality.
  
  ✅ Category Management
  Add custom expense categories with color-coded labels.
  
  ✅ Monthly & Yearly Summary Reports
  Generate PDF/print-friendly summaries of spending patterns.
  
  ✅ Email Notifications / Reminders
  Notify users about spending limits, summaries, or overdue expenses.
  
  ✅ Switch Database to PostgreSQL
  Make the app production-ready with a robust database.
  
  ✅ Improved Mobile UI
  Optimize experience further for smaller screen devices.
  
  ✅ PWA Support (Progressive Web App)
  Installable like a mobile app with offline support.
  
  ✅ Budget Planning & Goal Setting
  Let users plan a budget and track savings goals.



2. 🧠 Practice Projects & Code Archive

This repository contains my older works and practice code in Python (Flask) and Java, primarily from 2022–2023. It serves as a record of my early development efforts and learning journey.
- 🔹 [Practice-Projects ](https://github.com/Arunkumar2504/works)
## 🗂️ Contents

### 1. 🔥 Flask Project (2022)
- A basic web application built with Flask.
- Purpose: Learning backend routing, templates, and form handling in Python.
- Tech stack: Flask, HTML, basic CSS.

### 2. ☕ Java Practice Codes (2022–2023)
- Java programs written during my practice for concepts like:
  - Object-Oriented Programming (OOP)
  - Data structures (Array, Stack, Linked List, etc.)
  - File handling
  - Loops, conditionals, and core Java syntax

---

## 📌 Notes

- These are old personal learning projects and may not follow best practices or recent standards.
- For my current projects (like Django REST API / Expense Tracker), visit my other repositories.

## 🔗 Related Projects

- 💸 [Expense Tracker API + Dashboard (Django)](https://github.com/Arunkumar2504/expense-tracker)
  - Modern UI using TailwindCSS
  - REST API with pagination, filtering, charting
  - Export, Analytics, Mobile Responsive

---

## 📍 Future Updates

- Archive inactive projects
- Refactor and improve folder structure
- Add short descriptions to each file

  ---
3. SWE-Evaluation

This repository contains three Python scripts that automate tasks across Slack, JIRA, and Google Docs using simulated user activity.

✅ Task Overview
You are asked to:

Setup

Create free Google accounts for 3 users and share credentials.
Setup a free Slack Workspace and JIRA Project using the provided evalswe Gmail account.
Create:
5 Slack channels
2 JIRA projects
Python Automation

🟦 Slack: Simulate publishing messages from the 3 users.
🟧 JIRA: Simulate creating random issues from the 3 users.
🟩 Google Docs:
Create and share documents between all 3 users.
Add comments from 2 users.
Add reply from 3rd user.
Each script is responsible for automating one part of the evaluation:

Slack Automation (slack_message_bot.py)

Connects to Slack workspace
Sends messages to 5 channels from each user
JIRA Automation (create_jira_issues.py)

Logs into JIRA for each user
Creates random issues in the two projects
Google Docs Automation (main_user1.py)

Creates a Google Doc
Shares it between users
User 2 adds a comment
User 3 replies to the comment
🧪 Technologies Used

google-api-python-client for Google Docs/Drive
slack_sdk for Slack bot interaction
jira (Atlassian SDK) for JIRA integration

✅ Done
 Setup 3 Google accounts

 Create Slack workspace and channels

Slack name: https://sweevaluation.slack.com

Channels:

#announcements
#bugs
#daily_updates
#questions
#tasks
 Create 2 JIRA projects - Jira account: https://evalswe01.atlassian.net

 Automate interactions across platforms

 Exclude secrets from repo

▶️ How to Run
Run each script separately from the terminal:

python slack_message_bot.py
python create_jira_issues.py
python google_docs_script.py
python main_user1.py
A Note of Thanks
I would like to sincerely thank the team for this opportunity. Working on this evaluation allowed me to explore and learn more about integrating automation with collaborative tools like Slack, JIRA, and Google APIs. I truly admired the workflow and the way modern tools can be orchestrated using Python. It was a great learning experience.

----

