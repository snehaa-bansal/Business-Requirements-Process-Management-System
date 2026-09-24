# Functional Requirements Document (FRD)

## 1. Document Overview

### Project Name
Business Requirements & Process Management System

### Business Area
Human Resources – Employee Leave Management

### Purpose

This document defines the functional requirements of the proposed leave management system. These requirements describe the functionality that the system should provide to employees, managers, HR, and other authorized users.

---

## 2. User Roles

The system will support the following user roles:

### Employee
Can submit leave requests and track their status.

### Manager
Can view, approve, and reject leave requests submitted by employees.

### HR
Can view and manage employee leave records and access leave-related information.

### Management
Can view summarized leave information and reports.

---

# 3. Functional Requirements

## FR-01 – User Login

The system shall allow authorized users to log in using their credentials.

### Expected Behaviour

- User enters username/email and password.
- System validates the credentials.
- If credentials are valid, the user is logged in.
- If credentials are invalid, the system displays an appropriate error message.
- The system shall provide access according to the user's role.

---

## FR-02 – Employee Leave Request

The system shall allow employees to submit leave requests.

### Required Information

- Employee ID
- Leave Type
- Start Date
- End Date
- Reason

### Expected Behaviour

- Employee enters the required information.
- System validates the entered information.
- System creates a new leave request.
- The initial request status shall be set to "Pending".
- The employee shall receive a confirmation that the request has been submitted.

---

## FR-03 – Leave Request Validation

The system shall validate leave request information before submission.

### Validation Rules

- Leave type must be selected.
- Start date must be provided.
- End date must be provided.
- End date should not be earlier than the start date.
- Reason should be provided.
- Required fields must not be empty.

---

## FR-04 – View Leave Requests

The system shall allow authorized users to view leave requests according to their role.

### Employee

An employee can view their own submitted requests.

### Manager

A manager can view requests submitted by employees under their supervision.

### HR

HR can view employee leave records.

---

## FR-05 – Approve Leave Request

The system shall allow authorized managers to approve pending leave requests.

### Expected Behaviour

- Manager opens a pending request.
- Manager reviews the request details.
- Manager selects "Approve".
- System changes the request status to "Approved".
- The updated status becomes visible to the employee.

---

## FR-06 – Reject Leave Request

The system shall allow authorized managers to reject pending leave requests.

### Expected Behaviour

- Manager opens a pending request.
- Manager reviews the request details.
- Manager selects "Reject".
- System changes the request status to "Rejected".
- The updated status becomes visible to the employee.

---

## FR-07 – Leave Status Tracking

The system shall allow employees to track the status of their leave requests.

### Possible Statuses

- Pending
- Approved
- Rejected

---

## FR-08 – HR Leave Records

The system shall allow authorized HR users to view employee leave records.

HR should be able to view information such as:

- Employee ID
- Employee Name
- Leave Type
- Start Date
- End Date
- Reason
- Request Status

---

## FR-09 – Leave Reporting

The system shall provide leave-related information that can support basic reporting.

Reports may include:

- Total leave requests
- Pending requests
- Approved requests
- Rejected requests
- Leave requests by leave type
- Leave requests by employee

---

## FR-10 – Role-Based Access

The system shall restrict functionality according to user roles.

For example:

- Employees should only access their own leave requests.
- Managers should access requests relevant to their team.
- HR should access employee leave records.
- Management should access authorized reports.

---

# 4. Request Status Workflow

A leave request shall follow the following status flow:

Pending
   ↓
Manager Review
   ↓
Approved / Rejected

Once a request is approved or rejected, its status should be visible to the employee.

---

# 5. Functional Requirements Summary

| ID | Requirement | Primary User |
|---|---|---|
| FR-01 | User Login | All Users |
| FR-02 | Submit Leave Request | Employee |
| FR-03 | Validate Leave Request | Employee |
| FR-04 | View Leave Requests | Employee / Manager / HR |
| FR-05 | Approve Leave Request | Manager |
| FR-06 | Reject Leave Request | Manager |
| FR-07 | Track Leave Status | Employee |
| FR-08 | Manage Leave Records | HR |
| FR-09 | View Leave Reports | HR / Management |
| FR-10 | Role-Based Access | All Users |

---

# 6. Business Rules

The following business rules apply to the proposed system:

1. Only authorized users can access the system.
2. Employees can submit leave requests for themselves.
3. A new leave request will initially have a "Pending" status.
4. Only authorized managers can approve or reject requests.
5. An approved or rejected request cannot remain in the Pending state.
6. The end date of leave cannot be earlier than the start date.
7. Required information must be entered before a request can be submitted.
8. Users can only access information permitted by their role.