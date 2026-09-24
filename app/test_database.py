from database import get_user


user = get_user(
    "EMP001",
    "emp123"
)


if user:

    print("Login test successful!")

    print("User ID:", user[0])
    print("Name:", user[1])
    print("Role:", user[3])

else:

    print("Login test failed.")