"""Software user object"""
class User:
    """user class"""
    current_grade_book = None

    def __init__(self, first_name, last_name, email):
        """user initialization""" 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
