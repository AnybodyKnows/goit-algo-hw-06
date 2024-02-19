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
        if len(number) == 10:
            return number
        else:
            return False 

class Record:
    def __init__(self, name) -> None:
        self.value = name
        self.phones = []

    def add_phone(self, phone_number):
        number = Phone(phone_number)
        valid_number = number.validate_number(phone_number)
        if valid_number:
            self.phones.append(valid_number)

    def del_phone(self, phone_number):
        try: self.phones.remove(phone_number)
        except: pass

    def edit_phone(self, old_number, new_number):
        index = self.phones.index(old_number)
        self.phones[index] = new_number 

    def find_phone(self, phone_number):
        index = self.phones.index(phone_number)
        return self.phones[index]
    
    def __str__(self) -> str:
        return (f"Contact name:{self.value} phones:{self.phones}")    


class AddressBook(UserDict):

    def add_record(self, record_item):
        self.data[record_item.value] = record_item.phones
    
    def find(self, key):
        rec = Record(key)
        for x in self[key]:
            rec.add_phone(x)
        return rec

    def delete(self, key):
        del self[key]