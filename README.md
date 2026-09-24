# 📋 Business Requirements & Process Management System

A role-based Employee Leave Management System built using Python and Streamlit. The system allows employees to submit and track leave requests, while managers can review, approve/reject, filter, and monitor requests through a centralized dashboard.

## ✨ Features

### Employee
- Secure login
- Submit leave requests
- View submitted requests
- Track leave request status

### Manager
- Manager dashboard with request statistics
- View pending leave requests
- Approve or reject requests
- View all leave requests
- Filter requests by status
- Search requests using Employee ID
- View audit logs
- View business requirements

## 🔄 Workflow

Employee Login → Submit Leave Request → Request Stored in Database → Manager Reviews Request → Approve / Reject → Status Updated → Audit Log Created

## 🛠️ Tech Stack

- Python
- Streamlit
- SQLite
- Pandas
- Plotly
- HTML/CSS

## 🗄️ Database

The application uses SQLite for persistent data storage.

Main tables:
- `users`
- `employees`
- `leave_requests`
- `audit_logs`

## 📋 Business Requirements

- BR-01: Secure employee login
- BR-02: Submit leave requests
- BR-03: View submitted requests
- BR-04: Manager access to pending requests
- BR-05: Approve/reject leave requests
- BR-06: View all leave requests
- BR-07: Filter requests by status
- BR-08: Search using Employee ID
- BR-09: Maintain audit trail
- BR-10: Dashboard statistics
- BR-11: Update request status after approval/rejection
- BR-12: Persistent database storage

## 🚀 How to Run

1. Install dependencies:

    pip install -r requirements.txt

2. Run the application:

    streamlit run app/app.py

## 👤 Demo Credentials

Employee:
`EMP001` / `emp123`

Manager:
`MGR001` / `mgr123`

## 📁 Project Structure

Business-Requirements-Process-Management-System/
- app/
  - app.py
  - database.py
  - check_database.py
  - style.css
- requirements.txt
- README.md

## 🎯 Objective

The objective of this project is to provide a centralized digital workflow for employee leave management, including request submission, managerial approval, status tracking, persistent storage, and audit logging.

## 👩‍💻 Author

**Sneha Bansal**

B.Tech CSE – AI & ML