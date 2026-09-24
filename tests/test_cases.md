# Test Cases

## Project
Business Requirements & Process Management System

## Purpose

These test cases are used to verify whether the proposed system satisfies the documented functional requirements and acceptance criteria.

---

## TC-01 – Valid User Login

**Requirement:** FR-01

**Objective:** Verify that an authorized user can log into the system.

### Test Data
- Valid username/email
- Valid password

### Steps
1. Open the login page.
2. Enter valid username/email.
3. Enter valid password.
4. Click Login.

### Expected Result
The user should be successfully logged in and redirected to the appropriate dashboard based on their role.

### Expected Status
PASS

---

## TC-02 – Invalid User Login

**Requirement:** FR-01

**Objective:** Verify that invalid credentials are rejected.

### Steps
1. Open the login page.
2. Enter an invalid username or password.
3. Click Login.

### Expected Result
The system should reject the login attempt and display an appropriate error message.

### Expected Status
PASS

---

## TC-03 – Submit Valid Leave Request

**Requirement:** FR-02

**Objective:** Verify that an employee can submit a valid leave request.

### Test Data

- Employee ID: EMP001
- Leave Type: Casual Leave
- Start Date: 2026-10-05
- End Date: 2026-10-06
- Reason: Personal work

### Steps
1. Login as an employee.
2. Open the Leave Request section.
3. Enter valid leave details.
4. Click Submit.

### Expected Result
The system should create the leave request and assign it a Pending status.

### Expected Status
PASS

---

## TC-04 – Submit Leave Request with Missing Information

**Requirement:** FR-03

**Objective:** Verify that required fields are validated.

### Steps
1. Login as an employee.
2. Open the Leave Request form.
3. Leave one or more required fields empty.
4. Click Submit.

### Expected Result
The system should not create the request and should display an appropriate validation message.

### Expected Status
PASS

---

## TC-05 – Invalid Leave Date Range

**Requirement:** FR-03

**Objective:** Verify that the system prevents an invalid date range.

### Steps
1. Login as an employee.
2. Enter a start date.
3. Enter an end date earlier than the start date.
4. Submit the request.

### Expected Result
The system should reject the request and display a validation message.

### Expected Status
PASS

---

## TC-06 – View Leave Request Status

**Requirement:** FR-07

**Objective:** Verify that an employee can view the status of a submitted leave request.

### Steps
1. Login as an employee.
2. Open Leave History.
3. Locate a submitted leave request.

### Expected Result
The system should display the request and its current status.

### Expected Status
PASS

---

## TC-07 – Manager Views Pending Requests

**Requirement:** FR-04

**Objective:** Verify that a manager can view pending requests relevant to their team.

### Steps
1. Login as a manager.
2. Open Pending Requests.
3. View the available requests.

### Expected Result
The system should display relevant pending leave requests with their details.

### Expected Status
PASS

---

## TC-08 – Manager Approves Leave Request

**Requirement:** FR-05

**Objective:** Verify that a manager can approve a pending request.

### Steps
1. Login as a manager.
2. Open a pending leave request.
3. Review the request.
4. Click Approve.

### Expected Result
The request status should change from Pending to Approved.

### Expected Status
PASS

---

## TC-09 – Manager Rejects Leave Request

**Requirement:** FR-06

**Objective:** Verify that a manager can reject a pending request.

### Steps
1. Login as a manager.
2. Open a pending leave request.
3. Review the request.
4. Click Reject.

### Expected Result
The request status should change from Pending to Rejected.

### Expected Status
PASS

---

## TC-10 – Employee Views Updated Status

**Requirement:** FR-07

**Objective:** Verify that the employee can see the manager's decision.

### Steps
1. Submit a leave request.
2. Manager approves or rejects the request.
3. Login as the employee.
4. Open Leave History.

### Expected Result
The employee should see the updated Approved or Rejected status.

### Expected Status
PASS

---

## TC-11 – HR Views Leave Records

**Requirement:** FR-08

**Objective:** Verify that HR can access employee leave records.

### Steps
1. Login as an authorized HR user.
2. Open Leave Records.
3. View available records.

### Expected Result
The system should display relevant employee leave information.

### Expected Status
PASS

---

## TC-12 – Leave Summary Report

**Requirement:** FR-09

**Objective:** Verify that authorized users can view leave summary information.

### Steps
1. Login as an authorized HR or management user.
2. Open the Reports section.
3. View the leave summary.

### Expected Result
The system should display relevant leave statistics including total, pending, approved, and rejected requests.

### Expected Status
PASS

---

## TC-13 – Role-Based Access

**Requirement:** FR-10

**Objective:** Verify that users can access functionality according to their assigned role.

### Steps
1. Login as an employee.
2. Attempt to access manager-only functionality.
3. Repeat using other user roles where applicable.

### Expected Result
Users should not be able to access functionality outside their authorized role.

### Expected Status
PASS

---

# Test Case Summary

| Test Case | Requirement | Scenario | Expected Result |
|---|---|---|---|
| TC-01 | FR-01 | Valid login | Login successful |
| TC-02 | FR-01 | Invalid login | Error displayed |
| TC-03 | FR-02 | Valid leave submission | Request created |
| TC-04 | FR-03 | Missing information | Validation error |
| TC-05 | FR-03 | Invalid dates | Request rejected |
| TC-06 | FR-07 | View status | Current status displayed |
| TC-07 | FR-04 | View pending requests | Requests displayed |
| TC-08 | FR-05 | Approve request | Status = Approved |
| TC-09 | FR-06 | Reject request | Status = Rejected |
| TC-10 | FR-07 | Updated status | Employee sees decision |
| TC-11 | FR-08 | HR records | Records displayed |
| TC-12 | FR-09 | Leave report | Summary displayed |
| TC-13 | FR-10 | Role access | Unauthorized access blocked |