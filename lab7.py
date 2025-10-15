# Create a base class person with attributes, name and age. Create a derived class employee that inherites from person and adds attribute employee_id and salary. Implement multi level inheritence with a class manager derived from employee with a department attribute. Implement multiple inheritence with a class trainer that inherits from employee and certification. Write appropriate method to display all details for each type of employee, create obj for each class and display their information.

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

# An online store has a bass class product and two derived classes, electronics (brand and warranty) and clothing (size and fabric_type) 

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display_details(self):
        print(f"Product Name: {self.name}, Price: {self.price}")

class Electronics(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty
    
    def display_details(self):
        super().display_details()
        print(f"Brand: {self.brand}, Warranty: {self.warranty} years")

class Clothing(Product):
    def __init__(self, name, price, size, fabric_type):
        super().__init__(name, price)
        self.size = size
        self.fabric_type = fabric_type
    
    def display_details(self):
        super().display_details()
        print(f"Size: {self.size}, Fabric: {self.fabric_type}")

print("\nElectronics")
e1 = Electronics("Smartphone", 50000, "Samsung", 2)
e1.display_details()

print("\nClothing")
c1 = Clothing("Shirt", 1200, "Large", "Cotton")
c1.display_details()

# A school has a person, teacher and a class teacher, each level adds its own property and method 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def display_details(self):
        super().display_details()
        print(f"Subject: {self.subject}")
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

class ClassTeacher(Teacher):
    def __init__(self, name, age, subject, class_name):
        super().__init__(name, age, subject)
        self.class_name = class_name
    
    def display_details(self):
        super().display_details()
        print(f"Class Teacher of: {self.class_name}")
    
    def manage_class(self):
        print(f"{self.name} is managing class {self.class_name}.")

print("\nPerson")
p1 = Person("Anay", 30)
p1.display_details()

print("\nTeacher")
t1 = Teacher("Aditya", 40, "Mathematics")
t1.display_details()
t1.teach()

print("\nClass Teacher")
ct1 = ClassTeacher("Aarik", 45, "Science", "10th Grade")
ct1.display_details()
ct1.teach()
ct1.manage_class()
