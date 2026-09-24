import sqlite3


DATABASE_FILE = "data/leave_management.db"


# Connect to database
connection = sqlite3.connect(DATABASE_FILE)

cursor = connection.cursor()


# ==========================================
# CHECK TABLES
# ==========================================

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
""")

tables = cursor.fetchall()

print("\nTables in database:")

for table in tables:
    print("-", table[0])


# ==========================================
# CHECK USERS
# ==========================================

cursor.execute("""
    SELECT * FROM users
""")

users = cursor.fetchall()

print("\nUsers:")

for user in users:
    print(user)


# ==========================================
# CHECK EMPLOYEES
# ==========================================

cursor.execute("""
    SELECT * FROM employees
""")

employees = cursor.fetchall()

print("\nEmployees:")

for employee in employees:
    print(employee)


# ==========================================
# CHECK LEAVE REQUESTS
# ==========================================

cursor.execute("""
    SELECT * FROM leave_requests
""")

requests = cursor.fetchall()

print("\nLeave Requests:")

for request in requests:
    print(request)



print("\nAudit Logs:")

cursor.execute("""
    SELECT
        log_id,
        request_id,
        user_id,
        action,
        action_time
    FROM audit_logs
    ORDER BY log_id
""")

for row in cursor.fetchall():

    print(row)

# Close connection
connection.close()