# Defining Employee Class

class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
    
    # Getting the values to return
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    
    class ProductionWorker:
        def __init__ (self, name, number, shift_num, pay_rate):
            Employee.__init__(self, name, number)
            self.__shift_num = shift_num
            self.__pay_rate = pay_rate
        # Defining set methods for shift number and pay
        def set_shift_num(self, shift_num):
            self.__shift_num = shift_num
        def set_pay_rate(self, pay_rate):
            self.__pay_rate = pay_rate

        # Get method for program
        def get_shift_num(self):
            return self.__shift_num
        def get_pay_rate(self):
            return self.__pay_rate

# Prompting user to enter their name, number, shift number, and pay.
def main():
    print('Enter the corresponding details please.')
    name = input('Name: ')
    number = input('Employee Number: ')
    sn = input('Shift Number: ')
    pay_rate = input('Pay Rate Per Hour:')
    
    class Employee(str): (name, number, sn, pay_rate)
# Displaying results for the user based on the entered information.
    print('Here is the corresponding Employee information: ')
    print('Name:',Employee(name))
    print('Employee Number',Employee(number))
    print('Shift Number:', Employee(sn))
    print('Pay Rate:', Employee(pay_rate))
main()