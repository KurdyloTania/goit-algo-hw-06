from field import Field

class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError("Error: You need to enter a 10-digit phone number!!!")
        