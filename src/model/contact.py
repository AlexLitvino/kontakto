class Contact:

    def __init__(self, name, description=''):
        self.name = name
        self.description = description
        self.phones = []

    def add_phone(self, entered_form, description=''):
        self.phones.append(Phone(entered_form, description))
