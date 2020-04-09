class Employee:
    def __init__(self, fname, lname, add, phone):
        self.first_name = str(fname)
        self.last_name = str(lname)
        self.address = str(add)
        self.phone_number = str(phone)

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, add):
        self.address = add

    def set_phone_number(self, phone):
        self.phone_number = phone

    def display(self):
        message = str(self.first_name) + " " + str(self.last_name) + "\n" + str(self.address) + "\n"
        return message