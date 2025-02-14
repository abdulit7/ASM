import re



class Validation:
    def __init__(self) -> None:
        pass

    def validate_email(self, email):
        patren = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if not re.match(patren, email):
            return False
        
    def valid_password(self, password):
        if len(password) < 8:
            return False
    
        if not any(char.isdigit() for char in password):
            return False
        
        if not re.search("[A-Z]", password):
            return False
        
        return True
    
    