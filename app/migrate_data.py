import sqlite3
import pandas as pd


DATABASE_FILE = "data/leave_management.db"

USERS_FILE = "data/users.csv"
LEAVE_FILE = "data/sample_leave_data.csv"


def migrate_data():

    # ==========================================
    # CONNECT TO DATABASE
    # ==========================================

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    # ==========================================
    # CREATE CORRECT TABLE STRUCTURE
    # ==========================================

    cursor.execute("""
        DROP TABLE IF EXISTS users
    """)

    cursor.execute("""
        DROP TABLE IF EXISTS employees
    """)

    cursor.execute("""
        DROP TABLE IF EXISTS leave_requests
    """)

    # USERS TABLE

    cursor.execute("""
        CREATE TABLE users (
            user_id TEXT PRIMARY KEY,
            user_name TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            department TEXT
        )
    """)

    # EMPLOYEES TABLE

    cursor.execute("""
        CREATE TABLE employees (
            employee_id TEXT PRIMARY KEY,
            employee_name TEXT NOT NULL,
            department TEXT,
            manager_id TEXT
        )
    """)

    # LEAVE REQUESTS TABLE

    cursor.execute("""
        CREATE TABLE leave_requests (
            request_id TEXT PRIMARY KEY,
            employee_id TEXT NOT NULL,
            leave_type TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            reason TEXT NOT NULL,
            status TEXT NOT NULL,
            manager_id TEXT
        )
    """)

    connection.commit()

    print("Database tables created successfully.")

    # ==========================================
    # LOAD USERS
    # ==========================================

    users_df = pd.read_csv(USERS_FILE)

    for _, row in users_df.iterrows():

        cursor.execute("""
            INSERT INTO users
            (
                user_id,
                user_name,
                password,
                role,
                department
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            row["user_id"],
            row["user_name"],
            row["password"],
            row["role"],
            row["department"]
        ))

    print("Users data migrated successfully.")

    # ==========================================
    # LOAD LEAVE DATA
    # ==========================================

    leave_df = pd.read_csv(LEAVE_FILE)

    for _, row in leave_df.iterrows():

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
            row["request_id"],
            row["employee_id"],
            row["leave_type"],
            row["start_date"],
            row["end_date"],
            row["reason"],
            row["status"],
            "MGR001"
        ))

    print("Leave request data migrated successfully.")

    # ==========================================
    # CREATE EMPLOYEE DATA
    # ==========================================

    employee_columns = [
        "employee_id",
        "employee_name",
        "department"
    ]

    employees_df = leave_df[
        employee_columns
    ].drop_duplicates()

    for _, row in employees_df.iterrows():

        cursor.execute("""
            INSERT OR IGNORE INTO employees
            (
                employee_id,
                employee_name,
                department,
                manager_id
            )
            VALUES (?, ?, ?, ?)
        """, (
            row["employee_id"],
            row["employee_name"],
            row["department"],
            "MGR001"
        ))

    print("Employee data migrated successfully.")

    # ==========================================
    # SAVE
    # ==========================================

    connection.commit()

    connection.close()

    print("Data migration completed successfully.")


if __name__ == "__main__":

    migrate_data()