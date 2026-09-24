# Acceptance Criteria

## Project
Business Requirements & Process Management System

Acceptance criteria define the conditions that must be satisfied for a user story to be considered complete.

---

# US-01 – Submit Leave Request

### User Story

As an employee, I want to submit a leave request through the system so that I can apply for leave without sending an email.

### Acceptance Criteria

**AC-01**
Given the employee is logged in,

When the employee opens the leave request form,

Then the system should display the required leave fields.

**AC-02**
Given the employee has entered all required information,

When the employee submits the request,

Then the system should validate the information.

**AC-03**
Given the information is valid,

When the request is submitted,

Then the system should create the leave request with a "Pending" status.

**AC-04**
Given required information is missing,

When the employee submits the form,

Then the system should display an appropriate validation message.

---

# US-02 – View Leave Request Status

### User Story

As an employee, I want to view the status of my leave requests so that I know whether my request is pending, approved, or rejected.

### Acceptance Criteria

**AC-05**
Given the employee is logged in,

When the employee opens the leave history,

Then the system should display the employee's submitted requests.

**AC-06**
The system should display the current status of each request.

**AC-07**
The status should be one of:

- Pending
- Approved
- Rejected

---

# US-04 – View Pending Requests

### User Story

As a manager, I want to view pending leave requests from my team so that I can review them before making a decision.

### Acceptance Criteria

**AC-08**
Given the manager is logged in,

When the manager opens the pending requests section,

Then the system should display pending requests belonging to the manager's team.

**AC-09**
Each request should display relevant information such as:

- Employee name
- Leave type
- Start date
- End date
- Reason
- Current status

---

# US-05 – Approve Leave Request

### User Story

As a manager, I want to approve a valid leave request so that the employee can receive approval through the system.

### Acceptance Criteria

**AC-10**
Given a leave request has a Pending status,

When the manager selects Approve,

Then the system should change the request status to Approved.

**AC-11**
The updated status should be visible to the employee.

---

# US-06 – Reject Leave Request

### User Story

As a manager, I want to reject a leave request when it cannot be approved so that the employee receives a clear decision.

### Acceptance Criteria

**AC-12**
Given a leave request has a Pending status,

When the manager selects Reject,

Then the system should change the request status to Rejected.

**AC-13**
The updated status should be visible to the employee.

---

# US-07 – View Employee Leave Records

### User Story

As an HR user, I want to view employee leave records so that I can maintain centralized and accurate leave information.

### Acceptance Criteria

**AC-14**
Given an authorized HR user is logged in,

When the HR user opens the leave records section,

Then the system should display employee leave information.

**AC-15**
The records should include relevant fields such as:

- Employee ID
- Employee Name
- Leave Type
- Start Date
- End Date
- Reason
- Status

---

# US-08 – Monitor Leave Information

### User Story

As an HR user, I want to view leave-related information and statistics so that I can monitor leave activity and prepare reports.

### Acceptance Criteria

**AC-16**
The system should display the total number of leave requests.

**AC-17**
The system should display pending, approved, and rejected requests separately.

**AC-18**
The system should provide basic leave information by leave type.

---

# US-09 – View Leave Summary

### User Story

As a management user, I want to view summarized leave information so that I can understand workforce availability and leave trends.

### Acceptance Criteria

**AC-19**
Authorized management users should be able to access leave summary information.

**AC-20**
The summary should provide useful information such as total requests and request status distribution.

---

# US-10 – Role-Based Access

### User Story

As a system administrator, I want users to access functionality according to their roles so that sensitive leave information is protected.

### Acceptance Criteria

**AC-21**
Employees should only be able to access their own leave information.

**AC-22**
Managers should be able to access requests relevant to their team.

**AC-23**
HR users should be able to access authorized employee leave records.

**AC-24**
Users should not be able to access functionality that is outside their assigned role.