from collections import UserDict

class Record:
    def __init__(self, value) -> None:
        self.value = value
    
    def add_phone(self, phone_number):
        pass

class AddressBook(UserDict):
    def add_record(self, key, value):
        self.data[key]= value