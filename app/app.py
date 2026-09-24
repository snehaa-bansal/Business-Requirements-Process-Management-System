import streamlit as st
import os
import pandas as pd
import plotly.express as px
from datetime import date
from database import (
    get_connection,
    get_user,
    get_employee_requests,
    create_leave_request,
    get_all_requests,
    get_pending_requests,
    update_leave_status,
    get_request_statistics,
    log_audit_action,
    get_audit_logs
)

st.set_page_config(
    page_title="Leave Management System",
    page_icon="📋",
    layout="wide"
)

from pathlib import Path
# ================================
# LOAD CUSTOM CSS
# ================================

css_file = Path(__file__).parent / "style.css"

with open(css_file, "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# -----------------------------
# PAGE CONFIGURATION
# -----------------------------




st.divider()
# -----------------------------
# FILE PATH
# -----------------------------

DATA_FILE = "data/sample_leave_data.csv"

df = pd.read_csv(DATA_FILE)


# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv(DATA_FILE)


# -----------------------------
# HELPER FUNCTION
# -----------------------------

def save_data(dataframe):
    dataframe.to_csv(DATA_FILE, index=False)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None
# -----------------------------
# TITLE
# -----------------------------
# -----------------------------
# LOGIN SCREEN
# -----------------------------

# ==========================================
# LOGIN SCREEN
# ==========================================

if not st.session_state.logged_in:


      st.markdown("""
<div style="text-align:center; padding:35px 10px 20px;">
<div style="font-size:52px; margin-bottom:8px;">📋</div>
<div style="font-size:34px; font-weight:800; color:#20254d; letter-spacing:-1px;">
Leave Management System
</div>
<div style="font-size:15px; color:#737b98; margin-top:8px;">
Smart • Simple • Centralized
</div>
</div>
""", unsafe_allow_html=True)

      st.subheader("Login")

      user_id = st.text_input(
        "User ID",
        placeholder="Example: EMP001"
    )

      password = st.text_input(
        "Password",
        type="password"
    )

      login_button = st.button(
        "Login",
        type="primary"
    )

      if login_button:

        user = get_user(
            user_id,
            password
        )

        if user is not None:

            user_data = {
                "user_id": user[0],
                "user_name": user[1],
                "password": user[2],
                "role": user[3],
                "department": user[4]
            }

            st.session_state.logged_in = True
            st.session_state.user = user_data

            st.success(
                "Login successful!"
            )

            st.rerun()

        else:

            st.error(
                "Invalid User ID or Password."
            )

      st.stop()


st.title("📋 Employee Leave Management System")

st.write(
    "A centralized system for managing employee leave requests, "
    "approvals, records, and reporting."
)


# -----------------------------
# SIDEBAR
# -----------------------------

# -----------------------------
# LOGGED-IN USER
# -----------------------------

user = st.session_state.user

role = user["role"]
user_name = user["user_name"]
user_id = user["user_id"]

st.sidebar.title("Navigation")

st.sidebar.write(
    f"👤 **{user_name}**"
)

st.sidebar.write(
    f"Role: **{role}**"
)

st.sidebar.write("---")

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False
    st.session_state.user = None

    st.rerun()
# ============================================================
# EMPLOYEE MODULE
# ============================================================

class manager_menu:
    ...

if role == "Employee":

    menu = st.sidebar.radio(
        "Employee Menu",
        ["Dashboard", "Apply Leave", "My Requests"]
    )

    # -------------------------
    # EMPLOYEE DASHBOARD
    # -------------------------

    if menu == "Dashboard":

        st.header("👩‍💼 Employee Dashboard")

        st.info(
            "Use the sidebar to submit a leave request "
            "or view your previous requests."
        )

     # -------------------------
    # APPLY LEAVE
    # -------------------------

    elif menu == "Apply Leave":

        st.header("📝 Apply for Leave")

        st.write(
            "Enter the required information to submit a leave request."
        )

        employee_id = user["user_id"]

        st.write(
            f"**Employee ID:** {employee_id}"
        )

        employee_name = user["user_name"]

        st.write(
            f"**Employee Name:** {employee_name}"
        )

        leave_type = st.selectbox(
            "Leave Type",
            [
                "Casual Leave",
                "Sick Leave",
                "Annual Leave",
                "Emergency Leave"
            ]
        )

        start_date = st.date_input(
            "Start Date",
            min_value=date.today()
        )

        end_date = st.date_input(
            "End Date",
            min_value=date.today()
        )

        reason = st.text_area(
            "Reason",
            placeholder="Enter the reason for leave..."
        )

        submit = st.button(
            "Submit Leave Request",
            type="primary"
        )

        # -------------------------
        # FORM VALIDATION
        # -------------------------

        if submit:

            if employee_id.strip() == "":
                st.error("Please enter Employee ID.")

            elif employee_name.strip() == "":
                st.error("Please enter Employee Name.")

            elif reason.strip() == "":
                st.error("Please enter the reason for leave.")

            elif end_date < start_date:
                st.error(
                    "End date cannot be earlier than start date."
                )

            else:

                # -------------------------
                # GENERATE REQUEST ID
                # -------------------------

                existing_requests = get_all_requests()

                new_number = len(existing_requests) + 1

                request_id = f"LR{new_number:03d}"

                # -------------------------
                # CREATE LEAVE REQUEST
                # -------------------------

                create_leave_request(
                    request_id=request_id,
                    employee_id=employee_id,
                    leave_type=leave_type,
                    start_date=str(start_date),
                    end_date=str(end_date),
                    reason=reason,
                    manager_id="MGR001"
                )

                # -------------------------
                # SUCCESS MESSAGE
                # -------------------------

                st.success(
                    "✅ Leave request submitted successfully!"
                )

                st.write(
                    f"**Request ID:** {request_id}"
                )

                st.write(
                    "**Status:** Pending"
                )

    # -------------------------
    # MY REQUESTS
    # -------------------------

    elif menu == "My Requests":

     st.header("📄 My Leave Requests")

    employee_id = user["user_id"]

    requests = get_employee_requests(
        employee_id
    )

    if len(requests) == 0:

        st.info(
            "You have not submitted any leave requests yet."
        )

    else:

     requests_df = pd.DataFrame(
    requests,
    columns=[
        "Request ID",
        "Employee ID",
        "Leave Type",
        "Start Date",
        "End Date",
        "Reason",
        "Status",
        "Manager ID"
    ]
)

    st.dataframe(
            requests_df,
            use_container_width=True,
            hide_index=True
        )

# ============================================================
# MANAGER MODULE
# ============================================================

# ========================================================
# MANAGER ROLE
# ========================================================

elif role == "Manager":

    st.header("👨‍💼 Manager Dashboard")

    manager_menu = st.sidebar.radio(
        "Manager Menu",
        [
            "Dashboard",
            "Pending Requests",
            "All Requests",
            "Audit Logs",
            "Business Requirements"
        ]
    )

    # ========================================================
    # MANAGER DASHBOARD
    # ========================================================

    if manager_menu == "Dashboard":

        st.subheader("📊 Manager Overview")

        statistics = get_request_statistics()

        total_requests = statistics[0] or 0
        pending_requests = statistics[1] or 0
        approved_requests = statistics[2] or 0
        rejected_requests = statistics[3] or 0

        # -------------------------
        # KPI CARDS
        # -------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Requests",
                total_requests
            )

        with col2:
            st.metric(
                "Pending",
                pending_requests
            )

        with col3:
            st.metric(
                "Approved",
                approved_requests
            )

        with col4:
            st.metric(
                "Rejected",
                rejected_requests
            )

        # -------------------------
        # STATUS CHART
        # -------------------------

        st.divider()

        st.subheader("📈 Leave Request Status")

        status_data = pd.DataFrame({
            "Status": [
                "Pending",
                "Approved",
                "Rejected"
            ],
            "Requests": [
                pending_requests,
                approved_requests,
                rejected_requests
            ]
        })

        fig = px.bar(
            status_data,
            x="Status",
            y="Requests",
            title="Leave Requests by Status",
            text="Requests"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ========================================================
    # PENDING REQUESTS
    # ========================================================

    elif manager_menu == "Pending Requests":

        st.subheader("📋 Pending Leave Requests")

        pending_requests = get_pending_requests()

        if len(pending_requests) == 0:

            st.success(
                "There are no pending leave requests."
            )

        else:

            pending_df = pd.DataFrame(
                pending_requests,
                columns=[
                    "Request ID",
                    "Employee ID",
                    "Employee Name",
                    "Department",
                    "Leave Type",
                    "Start Date",
                    "End Date",
                    "Reason",
                    "Status",
                    "Manager ID"
                ]
            )

            st.dataframe(
                pending_df,
                use_container_width=True,
                hide_index=True
            )

            st.divider()

            st.subheader("🔎 Review Request")

            request_id = st.selectbox(
                "Select Request ID",
                pending_df["Request ID"].tolist()
            )

            selected_request = pending_df[
                pending_df["Request ID"] == request_id
            ].iloc[0]

            st.write(
                f"**Employee ID:** "
                f"{selected_request['Employee ID']}"
            )

            st.write(
                f"**Employee Name:** "
                f"{selected_request['Employee Name']}"
            )

            st.write(
                f"**Department:** "
                f"{selected_request['Department']}"
            )

            st.write(
                f"**Leave Type:** "
                f"{selected_request['Leave Type']}"
            )

            st.write(
                f"**Start Date:** "
                f"{selected_request['Start Date']}"
            )

            st.write(
                f"**End Date:** "
                f"{selected_request['End Date']}"
            )

            st.write(
                f"**Reason:** "
                f"{selected_request['Reason']}"
            )

            st.write(
                f"**Current Status:** "
                f"{selected_request['Status']}"
            )

            col1, col2 = st.columns(2)

            with col1:

                approve = st.button(
                    "✅ Approve Request",
                    use_container_width=True
                )

            with col2:

                reject = st.button(
                    "❌ Reject Request",
                    use_container_width=True
                )

            # -------------------------
            # APPROVE REQUEST
            # -------------------------

            if approve:

                update_leave_status(
                    request_id,
                    "Approved"
                )

                log_audit_action(
                    request_id,
                    user["user_id"],
                    "Approved"
                )

                st.success(
                    f"Request {request_id} has been approved."
                )

                st.rerun()

            # -------------------------
            # REJECT REQUEST
            # -------------------------

            if reject:

                update_leave_status(
                    request_id,
                    "Rejected"
                )

                log_audit_action(
                    request_id,
                    user["user_id"],
                    "Rejected"
                )

                st.error(
                    f"Request {request_id} has been rejected."
                )

                st.rerun()

    # ========================================================
    # ALL REQUESTS
    # ========================================================

    elif manager_menu == "All Requests":

        st.subheader("📄 All Leave Requests")

        all_requests = get_all_requests()

        if len(all_requests) == 0:

            st.info(
                "No leave requests found."
            )

        else:

            all_requests_df = pd.DataFrame(
                all_requests,
                columns=[
                    "Request ID",
                    "Employee ID",
                    "Employee Name",
                    "Department",
                    "Leave Type",
                    "Start Date",
                    "End Date",
                    "Reason",
                    "Status",
                    "Manager ID"
                ]
            )

            # -------------------------
            # FILTER
            # -------------------------

            status_filter = st.selectbox(
                "Filter by Status",
                [
                    "All",
                    "Pending",
                    "Approved",
                    "Rejected"
                ]
            )

            if status_filter != "All":

                all_requests_df = all_requests_df[
                    all_requests_df["Status"] == status_filter
                ]

            # -------------------------
            # SEARCH
            # -------------------------

            employee_search = st.text_input(
                "🔍 Search by Employee ID",
                placeholder="Example: EMP001"
            )

            if employee_search.strip():

                all_requests_df = all_requests_df[
                    all_requests_df["Employee ID"]
                    .astype(str)
                    .str.contains(
                        employee_search.strip(),
                        case=False,
                        na=False
                    )
                ]

            # -------------------------
            # RECORD COUNT
            # -------------------------

            st.write(
                f"**Records Found:** {len(all_requests_df)}"
            )

            # -------------------------
            # TABLE
            # -------------------------

            st.dataframe(
                all_requests_df,
                use_container_width=True,
                hide_index=True
            )

    # ========================================================
    # AUDIT LOGS
    # ========================================================

    elif manager_menu == "Audit Logs":

        st.subheader("🕒 Audit Trail")

        st.write(
            "Track approval and rejection actions performed by managers."
        )

        logs = get_audit_logs()

        if len(logs) == 0:

            st.info(
                "No audit records found."
            )

        else:

            audit_df = pd.DataFrame(
                logs,
                columns=[
                    "Log ID",
                    "Request ID",
                    "User ID",
                    "Action",
                    "Action Time"
                ]
            )

            st.write(
                f"**Total Audit Records:** {len(audit_df)}"
            )

            st.dataframe(
                audit_df,
                use_container_width=True,
                hide_index=True
            )

    # ========================================================
    # BUSINESS REQUIREMENTS
    # ========================================================

    elif manager_menu == "Business Requirements":

        st.subheader("📋 Business Requirements")

        st.write(
            "The system supports the following business requirements:"
        )

        requirements = [
            "Employees can log in securely using their credentials.",
            "Employees can submit leave requests.",
            "Employees can view their submitted leave requests.",
            "Managers can view pending leave requests.",
            "Managers can approve or reject leave requests.",
            "Managers can view all leave requests.",
            "Managers can filter leave requests by status.",
            "Managers can search leave requests using Employee ID.",
            "The system maintains an audit trail of manager actions.",
            "The system provides dashboard statistics for leave requests.",
            "Leave request status is updated after manager approval or rejection.",
            "Leave request data is stored persistently in the database."
        ]

        for i, requirement in enumerate(
            requirements,
            start=1
        ):

            st.write(
                f"**BR-{i:02d}:** {requirement}"
            )
     # ========================================================
    # BUSINESS REQUIREMENTS
    # ========================================================

elif manager_menu == "Business Requirements":

        st.subheader("📋 Business Requirements")

        st.write(
            "Business requirements and process documentation "
            "for the Leave Request Management System."
        )

        st.divider()

        st.markdown("### 🎯 1. Business Objective")

        st.write(
            "The objective of this system is to digitize and "
            "streamline the employee leave management process. "
            "The system allows employees to submit leave requests "
            "and enables managers to review, approve, or reject "
            "those requests through a centralized platform."
        )

        st.markdown("### 👥 2. Stakeholders")

        stakeholders = pd.DataFrame({
            "Stakeholder": [
                "Employee",
                "Manager",
                "HR",
                "Management"
            ],
            "Responsibility": [
                "Submit and track leave requests",
                "Review, approve or reject requests",
                "Monitor employee leave information",
                "Monitor overall leave operations"
            ]
        })

        st.dataframe(
            stakeholders,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### ⚙️ 3. Functional Requirements")

        requirements = pd.DataFrame({
            "ID": [
                "FR-01",
                "FR-02",
                "FR-03",
                "FR-04",
                "FR-05",
                "FR-06",
                "FR-07",
                "FR-08",
                "FR-09"
            ],
            "Requirement": [
                "User authentication based on role",
                "Employee can submit leave requests",
                "Employee can track submitted requests",
                "Manager can view pending requests",
                "Manager can approve or reject requests",
                "Manager can view all requests",
                "System maintains request status",
                "System maintains an audit trail",
                "Dashboard displays request statistics"
            ]
        })

        st.dataframe(
            requirements,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### 📌 4. Business Rules")

        st.write("""
        • Leave type is mandatory.

        • Start date and end date are mandatory.

        • End date cannot be earlier than the start date.

        • Every new leave request starts with Pending status.

        • Only authorized managers can approve or reject requests.

        • Approved and rejected actions are recorded in the audit trail.

        • Each request is associated with an employee and manager.
        """)

        st.markdown("### 🔄 5. Leave Approval Process")

        st.code("""
Employee
   │
   ▼
Submit Leave Request
   │
   ▼
Pending
   │
   ▼
Manager Review
   │
   ├───────────────┐
   ▼               ▼
Approve           Reject
   │               │
   ▼               ▼
Approved         Rejected
   │               │
   └───────┬───────┘
           ▼
       Audit Log
           │
           ▼
        Dashboard
        """)

        st.markdown("### 📊 6. Reporting Requirements")

        st.write("""
        The manager dashboard should provide:

        • Total number of leave requests

        • Number of pending requests

        • Number of approved requests

        • Number of rejected requests

        • Request status visualization

        • Access to complete request history
        """)

        st.markdown("### 🔐 7. Security Requirements")

        st.write("""
        • Users should access features according to their roles.

        • Employees should only submit and track their own requests.

        • Manager actions should be recorded in audit logs.

        • Request information should be stored in the centralized database.
        """)
# ============================================================
# HR MODULE
# ============================================================

elif role == "HR":

    st.header("👩‍💼 HR Dashboard")

    menu = st.sidebar.radio(
        "HR Menu",
        ["Dashboard", "Employee Records", "Leave Reports"]
    )

    # -------------------------
    # HR DASHBOARD
    # -------------------------

    if menu == "Dashboard":

        st.subheader("HR Overview")

        total_requests = len(df)

        pending_requests = len(
            df[df["status"] == "Pending"]
        )

        approved_requests = len(
            df[df["status"] == "Approved"]
        )

        rejected_requests = len(
            df[df["status"] == "Rejected"]
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Requests",
                total_requests
            )

        with col2:
            st.metric(
                "Pending",
                pending_requests
            )

        with col3:
            st.metric(
                "Approved",
                approved_requests
            )

        with col4:
            st.metric(
                "Rejected",
                rejected_requests
            )

    # -------------------------
    # EMPLOYEE RECORDS
    # -------------------------

    elif menu == "Employee Records":

        st.subheader("📋 Employee Leave Records")

        st.write(
            "Search and filter employee leave records."
        )

        # Search employee
        search_name = st.text_input(
            "Search by Employee Name",
            placeholder="Example: Rahul"
        )

        # Department filter
        departments = [
            "All"
        ] + sorted(
            df["department"].dropna().unique().tolist()
        )

        selected_department = st.selectbox(
            "Filter by Department",
            departments
        )

        # Status filter
        statuses = [
            "All",
            "Pending",
            "Approved",
            "Rejected"
        ]

        selected_status = st.selectbox(
            "Filter by Status",
            statuses
        )

        # Start with complete dataset
        filtered_df = df.copy()

        # Apply name search
        if search_name.strip():

            filtered_df = filtered_df[
                filtered_df["employee_name"]
                .str.contains(
                    search_name,
                    case=False,
                    na=False
                )
            ]

        # Apply department filter
        if selected_department != "All":

            filtered_df = filtered_df[
                filtered_df["department"]
                == selected_department
            ]

        # Apply status filter
        if selected_status != "All":

            filtered_df = filtered_df[
                filtered_df["status"]
                == selected_status
            ]

        st.write(
            f"**Records Found:** {len(filtered_df)}"
        )

        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True
        )

    # -------------------------
    # LEAVE REPORTS
    # -------------------------

    elif menu == "Leave Reports":

        st.subheader("📊 Leave Reports")

        # Status summary
        status_summary = (
            df["status"]
            .value_counts()
            .reset_index()
        )

        status_summary.columns = [
            "Status",
            "Count"
        ]

        st.write("### Leave Status Summary")

        st.dataframe(
            status_summary,
            use_container_width=True,
            hide_index=True
        )

        # Status chart
        fig_status = px.bar(
            status_summary,
            x="Status",
            y="Count",
            title="Leave Requests by Status"
        )

        st.plotly_chart(
            fig_status,
            use_container_width=True
        )

        # Leave type analysis
        leave_type_summary = (
            df["leave_type"]
            .value_counts()
            .reset_index()
        )

        leave_type_summary.columns = [
            "Leave Type",
            "Count"
        ]

        st.write("### Leave Type Analysis")

        fig_leave_type = px.pie(
            leave_type_summary,
            names="Leave Type",
            values="Count",
            title="Leave Requests by Leave Type"
        )

        st.plotly_chart(
            fig_leave_type,
            use_container_width=True
        )

        # Department analysis
        department_summary = (
            df["department"]
            .value_counts()
            .reset_index()
        )

        department_summary.columns = [
            "Department",
            "Count"
        ]

        st.write("### Department-wise Requests")

        fig_department = px.bar(
            department_summary,
            x="Department",
            y="Count",
            title="Leave Requests by Department"
        )

        st.plotly_chart(
            fig_department,
            use_container_width=True
        )

# ============================================================
# MANAGEMENT MODULE
# ============================================================

# ============================================================
# MANAGEMENT MODULE
# ============================================================

elif role == "Management":

    st.header("📊 Management Dashboard")

    menu = st.sidebar.radio(
        "Management Menu",
        ["Overview", "Department Analysis", "Leave Analysis"]
    )

    # -------------------------
    # OVERVIEW
    # -------------------------

    if menu == "Overview":

        st.subheader("Business Overview")

        total_requests = len(df)

        pending_requests = len(
            df[df["status"] == "Pending"]
        )

        approved_requests = len(
            df[df["status"] == "Approved"]
        )

        rejected_requests = len(
            df[df["status"] == "Rejected"]
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Leave Requests",
                total_requests
            )

        with col2:
            st.metric(
                "Pending",
                pending_requests
            )

        with col3:
            st.metric(
                "Approved",
                approved_requests
            )

        with col4:
            st.metric(
                "Rejected",
                rejected_requests
            )

        st.divider()

        # Approval rate

        if total_requests > 0:

            approval_rate = (
                approved_requests / total_requests
            ) * 100

            st.metric(
                "Approval Rate",
                f"{approval_rate:.1f}%"
            )

    # -------------------------
    # DEPARTMENT ANALYSIS
    # -------------------------

    elif menu == "Department Analysis":

        st.subheader("🏢 Department-wise Leave Analysis")

        department_summary = (
            df.groupby("department")
            .size()
            .reset_index(name="Requests")
        )

        st.dataframe(
            department_summary,
            use_container_width=True,
            hide_index=True
        )

        fig_department = px.bar(
            department_summary,
            x="department",
            y="Requests",
            title="Leave Requests by Department",
            labels={
                "department": "Department",
                "Requests": "Number of Requests"
            }
        )

        st.plotly_chart(
            fig_department,
            use_container_width=True
        )

    # -------------------------
    # LEAVE ANALYSIS
    # -------------------------

    elif menu == "Leave Analysis":

        st.subheader("📈 Leave Type Analysis")

        leave_summary = (
            df.groupby("leave_type")
            .size()
            .reset_index(name="Requests")
        )

        st.dataframe(
            leave_summary,
            use_container_width=True,
            hide_index=True
        )

        fig_leave = px.pie(
            leave_summary,
            names="leave_type",
            values="Requests",
            title="Distribution of Leave Types"
        )

        st.plotly_chart(
            fig_leave,
            use_container_width=True
        )

        st.divider()

        st.subheader("Request Status Distribution")

        status_summary = (
            df["status"]
            .value_counts()
            .reset_index()
        )

        status_summary.columns = [
            "Status",
            "Requests"
        ]

        fig_status = px.bar(
            status_summary,
            x="Status",
            y="Requests",
            title="Leave Request Status"
        )

        st.plotly_chart(
            fig_status,
            use_container_width=True
        )

# ==========================================
# GET DASHBOARD STATISTICS
# ==========================================

def get_request_statistics():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total_requests,

            SUM(
                CASE
                    WHEN status = 'Pending'
                    THEN 1
                    ELSE 0
                END
            ) AS pending_requests,

            SUM(
                CASE
                    WHEN status = 'Approved'
                    THEN 1
                    ELSE 0
                END
            ) AS approved_requests,

            SUM(
                CASE
                    WHEN status = 'Rejected'
                    THEN 1
                    ELSE 0
                END
            ) AS rejected_requests

        FROM leave_requests
    """)

    result = cursor.fetchone()

    connection.close()

    return result