from collections import UserDict
import re


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
        if self.validate_number(number):
            super().__init__(number)
        else:
            raise ValueError
    
    def validate_number(self, number):
        if (len(number)==10) and \
            (re.match(r"^\d+$",number)):
            return True
        else:
            raise ValueError

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Phone):
            return self.value == other.value
        else:
            return False  

class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        number = Phone(phone_number)
        if number:
            self.phones.append(number)

    def remove_phone(self, phone_number):
        phone_obj = Phone(phone_number)
        for obj in self.phones:
            if obj.value == phone_obj.value:
                self.phones.remove(obj)

    def edit_phone(self, old_number, new_number):
        self.find_phone(old_number)
        self.remove_phone(old_number)
        self.add_phone(new_number)

    def find_phone(self, phone_number):
        ph = Phone(phone_number)
        if ph in self.phones:
            return ph
        else:
            raise ValueError

   
    def __str__(self) -> str:
        return (f"Contact name:{self.name.value} phones:{[obj.value for obj in self.phones]}")    

    
class AddressBook(UserDict):

    def add_record(self, record_item):
        self.data[record_item.name.value] = record_item
    
    def find(self, key):
        if key in self:
            return self[key]
        else: 
            raise KeyError

    def delete(self, key):
        if key in self:
            del self[key]
        else: 
            raise KeyError