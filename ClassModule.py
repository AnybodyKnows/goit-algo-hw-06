from collections import UserDict

class Field:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self):
        return self.value
    
class Name(Field):
    def __init__(self, value):
        if len(value) !=0:
            super().__init__(value)
        else: pass 
        
class Phone(Field):
    def __init__(self, number):
        if len(number) == 10:
            super().__init__(number)
        else:
            return False 

class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        number = Phone(phone_number)
        if number:
            self.phones.append(number.value)

    def remove_phone(self, phone_number):
        try: self.phones.remove(phone_number)
        except: pass

    def edit_phone(self, old_number, new_number):
        index = self.phones.index(old_number)
        self.phones[index] = new_number 

    def find_phone(self, phone_number):
        index = self.phones.index(phone_number)
        return self.phones[index]
    
    def __str__(self) -> str:
        return (f"Contact name:{self.name.value} phones:{self.phones}")    


class AddressBook(UserDict):

    def add_record(self, record_item):
        self.data[record_item.name.value] = record_item
    
    def find(self, key):
        return self[key]

    def delete(self, key):
        del self[key]