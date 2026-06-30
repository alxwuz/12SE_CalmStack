import json
import os
import hashlib

user_file = "users.json" # file for user and password data

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(user_file) or os.path.getsize(user_file) == 0: # if file isn't there give an empty list
        return {}
    with open(user_file, "r") as f: # read mode
        return json.load(f)

def save_users(users):
    with open(user_file, "w") as f:
        json.dump(users, f, indent=2)

def register_user(username, password):
    users = load_users()

    if username in users:
        return False, "Username already taken."

    users[username] = hash_password(password)
    save_users(users)
    return True, "Account created!"

def verify_user(username, password):
    users = load_users()

    if username not in users:
        return False, "No account with that username."

    if hash_password(password) == users[username]:
        return True, "Login successful!"
    else:
        return False, "Incorrect password."