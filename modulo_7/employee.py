# employee.py
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise by the specified amount."""
        self.salary += amount
    
    def get_salary(self):
        """Return the current salary."""
        return self.salary
    
    def describe_employee(self):
        """Display employee information."""
        print(f"{self.first_name} {self.last_name} - Salary: ${self.salary:,}")
    
    def get_full_name(self):
        """Return the employee's full name."""
        return f"{self.first_name} {self.last_name}"