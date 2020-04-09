from employee_stuff import employee as e
import datetime


class SalariedEmployee(e.Employee):
    def __init__(self, fname, lname, add, phone, start, salary):
        super().__init__(fname, lname, add, phone)
        self.start_date = start
        self.salary = float(salary)

    def give_raise(self, new_salary):
        "updates salary"
        self.salary = float(new_salary)

    def display(self):
        return str(self.first_name) + " " + str(self.last_name) + "\n" + str(self.address) + "\nStart Date: " + \
                   str(self.start_date.strftime("%Y-%m-%d")) + "\nSalary: $" + str(self.salary)


# Driver
sEmployee = SalariedEmployee("John", "Ryan", "1245 Elkwood Way", "555-555-5555", datetime.datetime.now(), 40000.0)
print(sEmployee.display() + "\n----------")
sEmployee.give_raise(45000)
print(sEmployee.display())
del sEmployee
