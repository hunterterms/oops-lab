# Create a base class person with attributes, name and age. Create a derieved class employee that inherites from person and adds attribute employee_id and salary. Implement multi level inheritence with a class manager derieved from employee with a department attribute. Implement multiple inheritence with a class trainer that inherits from employee and certification. Write appropriate method to display all details for each type of employee, create obj for each class and display their information.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    
    def display_details(self):
        super().display_details()
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department
    
    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")

class Certification:
    def __init__(self, certification):
        self.certification = certification
    
    def display_certification(self):
        print(f"Certification: {self.certification}")

class Trainer(Employee, Certification):
    def __init__(self, name, age, employee_id, salary, certification):
        Employee.__init__(self, name, age, employee_id, salary)
        Certification.__init__(self, certification)
    
    def display_details(self):
        Employee.display_details(self)
        Certification.display_certification(self)

print("Person")
p1 = Person("Aditya", 20)
p1.display_details()

print("\nEmployee")
e1 = Employee("Aarik", 20, "101", 50000)
e1.display_details()

print("\nManager")
m1 = Manager("Anay", 18, "102", 90000, "CSE")
m1.display_details()

print("\nTrainer")
t1 = Trainer("Ankit", 19, "103", 60000, "Python Certification")
t1.display_details()