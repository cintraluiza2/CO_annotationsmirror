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
            "num_articles_note": 0,
            "num_comments": 0,
            "comments": []
        }
                
    def get_dict(self):
        return self.model_doc
    