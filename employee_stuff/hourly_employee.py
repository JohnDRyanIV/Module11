from employee_stuff import employee as e
import datetime


class HourlyEmployee(e.Employee):
    def __init__(self, fname, lname, add, phone, start, hourly):
        super().__init__(fname, lname, add, phone)
        self.start_date = start
        self.hourly_pay = float(hourly)

    def give_raise(self, amount):
        self.hourly_pay = float(amount)

    def display(self):
        return str(self.first_name) + " " + str(self.last_name) + "\n" + str(self.address) + "\nStart Date: " + \
               str(self.start_date.strftime("%Y-%m-%d")) + "\nHourly Wage: $" + str(self.hourly_pay)


# Driver
hEmployee = HourlyEmployee("John", "Ryan", "1245 Elkwood Way", "555-555-5555", datetime.datetime.now(), 10.0)
print(hEmployee.display() + "\n----------")
hEmployee.give_raise(12.0)
print(hEmployee.display())
del hEmployee

