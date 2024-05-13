def email_valid(email):
    if '@' in email and '.' in email:
        return True
    return False 