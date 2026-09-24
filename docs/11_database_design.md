# Database Design

## 1. Overview

The Leave Management System uses a relational database design to store user,
employee, and leave request information in a structured manner.

The initial prototype used CSV files for rapid development. The proposed
database design uses SQLite to improve data organization, consistency,
relationships, and scalability.

---

## 2. Entities

The main entities are:

1. Users
2. Employees
3. Leave Requests

---

## 3. Users Table

The Users table stores login and role information.

| Field | Type | Description |
|---|---|---|
| user_id | TEXT | Unique user identifier |
| user_name | TEXT | Name of the user |
| password | TEXT | Login password for prototype |
| role | TEXT | Employee, Manager, HR, Management |
| department | TEXT | Department associated with user |

Primary Key: `user_id`

---

## 4. Employees Table

The Employees table stores organizational information.

| Field | Type | Description |
|---|---|---|
| employee_id | TEXT | Unique employee identifier |
| employee_name | TEXT | Employee name |
| department | TEXT | Employee department |
| manager_id | TEXT | ID of reporting manager |

Primary Key: `employee_id`

---

## 5. Leave Requests Table

The Leave Requests table stores leave applications and their current status.

| Field | Type | Description |
|---|---|---|
| request_id | TEXT | Unique leave request ID |
| employee_id | TEXT | Employee submitting request |
| leave_type | TEXT | Type of leave |
| start_date | DATE | Leave start date |
| end_date | DATE | Leave end date |
| reason | TEXT | Reason for leave |
| status | TEXT | Pending, Approved, Rejected |
| manager_id | TEXT | Manager responsible for request |

Primary Key: `request_id`

---

## 6. Relationships

### Employee → Leave Requests

One employee can submit multiple leave requests.

Therefore:

`Employee 1 : Many Leave Requests`

### Manager → Leave Requests

One manager can review multiple leave requests.

Therefore:

`Manager 1 : Many Leave Requests`

---

## 7. Simplified ER Diagram

```text
┌─────────────────────┐
│       USERS         │
├─────────────────────┤
│ PK user_id          │
│ user_name           │
│ password            │
│ role                │
│ department          │
└──────────┬──────────┘
           │
           │
           ↓
┌─────────────────────┐
│     EMPLOYEES       │
├─────────────────────┤
│ PK employee_id      │
│ employee_name       │
│ department          │
│ manager_id          │
└──────────┬──────────┘
           │
           │ 1
           │
           │
           │ *
           ↓
┌─────────────────────┐
│   LEAVE_REQUESTS    │
├─────────────────────┤
│ PK request_id       │
│ FK employee_id      │
│ leave_type          │
│ start_date          │
│ end_date            │
│ reason              │
│ status              │
│ manager_id          │
└─────────────────────┘