import bcrypt
import random
import string
import re

from ..data.database import user_exists, create_user

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def register_user(email, role):
    if user_exists(email):
        return False
    
    new_password = generate_password()

    role = {
        "Administrador": 1,
        "Anotador": 0,
    }[role]

    create_user(email, new_password, role)

    return new_password