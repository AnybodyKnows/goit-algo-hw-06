from collections import UserDict

class Field:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self):
        return self.value
    
class Name(Field):
    pass
        
class Phone(Field):
    def validate_number(self, number):
        if len(number) != 10:
            return self.phone == number
        else:
            return  

class Record:
    def __init__(self, name) -> None:
        self.value = name
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def del_phone(self, phone_number):
        try: self.phones.remove(phone_number)
        except: pass

    def edit_phone(self, old_number, new_number):
        pass

    def find_phone(self, phone_number):
        pass    


class AddressBook(UserDict):
    def add_record(self, key, value):
        self.data[key]= value
    
    def find_record(self, key):
        pass

    def del_record(self, key):
        pass