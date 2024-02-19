# Author: James Wiegman Date: 2/18/2024 -  Mailing List

class Person:
    # Initialize Object
    def __init__(self, name, address, phone):
            self.__name = name
            self.__address = address 
            self.__phone = phone

# Gather data about the user
name = input('Name: ')
address = input('Address: ')
phone = input('Phone: ')
customer_number = input('Customer number: ')
mail = input('Include in mailing list? (y/n): ')

# Determine True or False for Mailing List
if mail.lower() == 'y':
    mailing_list = True
else:
    mailing_list = False

# Must set a person class instance
class Person:
    # I have to initialize the object
    def __init__ (self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # Settting mutator for the __address attribute
    def set_mailing_list(self, address):
        self.__address = address
    
    # Setting mutator for the __phone attribute
    def set_phone(self, phone):
        self.__phone = phone

    # Setting an accessor with set for the __name attribute
    def set_name(self, name):
        self.__name = name
    
    # Setting an accessor to return __self attribute
    def get_name(self):
        return self.__name
    
    # Accessor for returning the __address attribute
    def get_address(self):
        return self.__phone
    

    # Customer Class
    class Customer:
        # Initializing the object class
        def __init__(self, name, address, phone, customer_number, mailing_list):
            # Super class for __init__
            Person.__init__(self, name, address, phone)

        # Initializing specialized attributes
            self.__customer_number = customer_number
            self.__mailing_list = mailing_list
    

    # Setting mutator for __customer_number
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number
    
    # Setting mutator for __mailing_list attribute
    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list