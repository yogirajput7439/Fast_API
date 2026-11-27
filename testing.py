from security import hash_password
from security import verify_password

password = "Rahul@123"

hashed = hash_password(password)

print("Original:", password)
print("Hashed:", hashed)

print("Correct password:", verify_password("Rahul@123", hashed))
print("Wrong password:", verify_password("WrongPassword", hashed))

