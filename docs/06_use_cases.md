# Use Cases

## Project
Business Requirements & Process Management System

Use cases describe the interaction between system users and the proposed leave management system.

---

# UC-01 – User Login

### Actor
Employee / Manager / HR / Management

### Goal
Allow an authorized user to securely access the system according to their role.

### Preconditions
- User must have valid login credentials.
- User must be registered in the system.

### Main Flow

1. User opens the login page.
2. User enters username/email.
3. User enters password.
4. User selects Login.
5. System validates the credentials.
6. System identifies the user's role.
7. System provides access to the appropriate dashboard.

### Alternative Flow

If the credentials are invalid:

1. System rejects the login attempt.
2. System displays an appropriate error message.
3. User can try again.

### Postcondition
The authorized user is logged into the system.

---

# UC-02 – Submit Leave Request

### Actor
Employee

### Goal
Allow an employee to submit a leave request.

### Preconditions
- Employee must be logged in.

### Main Flow

1. Employee opens the Leave Request section.
2. Employee selects the leave type.
3. Employee enters the start date.
4. Employee enters the end date.
5. Employee enters the reason for leave.
6. Employee submits the request.
7. System validates the entered information.
8. System creates the leave request.
9. System assigns the status "Pending".
10. System displays a confirmation message.

### Alternative Flow

If required information is missing or invalid:

1. System does not create the request.
2. System displays validation messages.
3. Employee corrects the information.
4. Employee submits the request again.

### Postcondition
A valid leave request is stored with Pending status.

---

# UC-03 – View Leave Request Status

### Actor
Employee

### Goal
Allow an employee to track submitted leave requests.

### Preconditions
- Employee must be logged in.
- Employee must have submitted at least one leave request.

### Main Flow

1. Employee opens the Leave History section.
2. System retrieves the employee's leave requests.
3. System displays the request details.
4. System displays the current status of each request.

### Possible Statuses

- Pending
- Approved
- Rejected

### Postcondition
Employee can view the current status of their leave requests.

---

# UC-04 – Review Leave Request

### Actor
Manager

### Goal
Allow a manager to review pending leave requests from their team.

### Preconditions
- Manager must be logged in.
- There must be pending requests associated with the manager's team.

### Main Flow

1. Manager opens the Pending Requests section.
2. System displays pending requests.
3. Manager selects a request.
4. System displays request details.
5. Manager reviews the leave information.
6. Manager chooses Approve or Reject.

### Postcondition
The manager has made a decision on the leave request.

---

# UC-05 – Approve Leave Request

### Actor
Manager

### Goal
Approve a valid employee leave request.

### Preconditions
- Manager must be logged in.
- Leave request must have Pending status.

### Main Flow

1. Manager opens a pending request.
2. Manager reviews the request.
3. Manager selects Approve.
4. System changes the request status to Approved.
5. System stores the updated status.
6. Employee can view the updated status.

### Postcondition
The leave request is marked as Approved.

---

# UC-06 – Reject Leave Request

### Actor
Manager

### Goal
Reject an employee leave request when it cannot be approved.

### Preconditions
- Manager must be logged in.
- Leave request must have Pending status.

### Main Flow

1. Manager opens a pending request.
2. Manager reviews the request.
3. Manager selects Reject.
4. System changes the request status to Rejected.
5. System stores the updated status.
6. Employee can view the updated status.

### Postcondition
The leave request is marked as Rejected.

---

# UC-07 – View Employee Leave Records

### Actor
HR

### Goal
Allow HR to view centralized employee leave records.

### Preconditions
- HR user must be logged in.
- HR user must have appropriate authorization.

### Main Flow

1. HR opens the Leave Records section.
2. System retrieves available leave records.
3. System displays employee leave information.
4. HR can review the records.

### Information Displayed

- Employee ID
- Employee Name
- Leave Type
- Start Date
- End Date
- Reason
- Status

### Postcondition
HR can access centralized leave records.

---

# UC-08 – View Leave Reports

### Actor
HR / Management

### Goal
Allow authorized users to view summarized leave information.

### Preconditions
- User must be authorized to access reports.

### Main Flow

1. User opens the Reports section.
2. System retrieves leave information.
3. System calculates relevant statistics.
4. System displays the summarized information.

### Example Information

- Total requests
- Pending requests
- Approved requests
- Rejected requests
- Requests by leave type

### Postcondition
Authorized users can access leave-related summary information.