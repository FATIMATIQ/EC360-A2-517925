import hashlib

users = {}


def register(email, password):
    if email in users:
        return "An account with this email already exists"
    users[email] = hashlib.sha256(password.encode()).hexdigest()
    return "Registered"