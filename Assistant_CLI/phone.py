from field import Field

class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)
        self.phone = phone
        if len(self.phone) != 10:
            raise ValueError("Error: You need to enter a 10-digit phone number!!!")
        self.value = self.phone