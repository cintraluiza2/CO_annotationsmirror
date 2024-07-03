from email_validator import validate_email, EmailNotValidError
import bcrypt

class Users():
    def __init__(self, first_name, last_name, email, password, role) -> None:
        validate_email(email)
        password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(10))
        self.model_doc = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "role": role,
            "notes": None,
            "num_article": 0,
            "id_article": {},
            "num_notes": 0,
            "notes": {}
        }
                
    def get_dict(self):
        return self.model_doc
    