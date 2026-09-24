import sqlite3


DATABASE_FILE = "data/leave_management.db"


def get_connection():
    return sqlite3.connect(DATABASE_FILE)


# ==========================================
# LOGIN
# ==========================================

def get_user(user_id, password):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_id, user_name, password, role, department
        FROM users
        WHERE user_id = ?
        AND password = ?
    """, (user_id, password))

    user = cursor.fetchone()

    connection.close()

    return user


# ==========================================
# CREATE LEAVE REQUEST
# ==========================================

def create_leave_request(
    request_id,
    employee_id,
    leave_type,
    start_date,
    end_date,
    reason,
    manager_id
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO leave_requests
        (
            request_id,
            employee_id,
            leave_type,
            start_date,
            end_date,
            reason,
            status,
            manager_id
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        request_id,
        employee_id,
        leave_type,
        start_date,
        end_date,
        reason,
        "Pending",
        manager_id
    ))

    connection.commit()

    connection.close()


# ==========================================
# GET EMPLOYEE REQUESTS
# ==========================================

def get_employee_requests(employee_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            request_id,
            employee_id,
            leave_type,
            start_date,
            end_date,
            reason,
            status,
            manager_id
        FROM leave_requests
        WHERE employee_id = ?
    """, (employee_id,))

    requests = cursor.fetchall()

    connection.close()

    return requests


# ==========================================
# GET PENDING REQUESTS
# ==========================================

# ==========================================
# GET PENDING LEAVE REQUESTS
# ==========================================

# ==========================================
# GET PENDING REQUESTS WITH EMPLOYEE DETAILS
# ==========================================

# ==========================================
# GET PENDING REQUESTS
# ==========================================

def get_pending_requests():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            lr.request_id,
            lr.employee_id,
            u.user_name,
            u.department,
            lr.leave_type,
            lr.start_date,
            lr.end_date,
            lr.reason,
            lr.status,
            lr.manager_id
        FROM leave_requests lr
        LEFT JOIN users u
            ON lr.employee_id = u.user_id
        WHERE lr.status = 'Pending'
        AND lr.manager_id = 'MGR001'
        ORDER BY lr.request_id
    """)

    requests = cursor.fetchall()

    connection.close()

    return requests
# ==========================================
# UPDATE LEAVE STATUS
# ==========================================

def update_leave_status(request_id, status):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE leave_requests
        SET status = ?
        WHERE request_id = ?
    """, (status, request_id))

    connection.commit()

    connection.close()


# ==========================================
# GET ALL LEAVE REQUESTS
# ==========================================

# ==========================================
# GET ALL LEAVE REQUESTS WITH EMPLOYEE DETAILS
# ==========================================

def get_all_requests():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            lr.request_id,
            lr.employee_id,
            e.employee_name,
            e.department,
            lr.leave_type,
            lr.start_date,
            lr.end_date,
            lr.reason,
            lr.status,
            e.manager_id
        FROM leave_requests lr
        LEFT JOIN employees e
            ON lr.employee_id = e.employee_id
        ORDER BY lr.request_id
    """)

    requests = cursor.fetchall()

    connection.close()

    return requests
# ==========================================
# GET LEAVE STATISTICS
# ==========================================

def get_status_counts():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT status, COUNT(*)
        FROM leave_requests
        GROUP BY status
    """)

    results = cursor.fetchall()

    connection.close()

    return results
# ==========================================
# GET REQUEST STATISTICS
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

# ==========================================
# AUDIT LOG
# ==========================================

def log_audit_action(request_id, user_id, action):

    class DB_PATH:
        ...

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO audit_logs
        (
            request_id,
            user_id,
            action,
            action_time
        )
        VALUES (?, ?, ?, datetime('now'))
        """,
        (
            request_id,
            user_id,
            action
        )
    )

    conn.commit()
    conn.close()

    # ==========================================
# GET AUDIT LOGS
# ==========================================

def get_audit_logs():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            log_id,
            request_id,
            user_id,
            action,
            action_time
        FROM audit_logs
        ORDER BY action_time DESC
    """)

    logs = cursor.fetchall()

    connection.close()

    return logs