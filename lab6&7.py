#Create a python class called bank account which represent a bank account having as attributes: acc no., name, balance Create a constructor with parameters: acc no., name, balance. Create a deposit method which manages the deposit actions. Create a withdrawal methods with manages withdrawal actions. Create a bank fees method to apply the bank fees with a % of 5% of the balance account. Create a display method to display the account details 

class bankAccount:
    def __init__(self, account, name, balance):
        self.account = account
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdrawal(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else: 
            print("Not enough money in your account")

    def bank_fees(self, amount):
        if amount<1000:
            self.balance = self.balance - self.balance*0.05
    
    def display(self):
        print(f"Name: {self.name} and Balance: {self.balance}")

Bank = bankAccount(101, "Someone", 1000)

Bank.deposit(10)
Bank.withdrawal(100)
Bank.display()

#Create 2 employees and print their salary slips. calculate_salary() method, returns total salary after adding DA (20%) and HRA (15%), display(), prints employee details with total salary

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def calculate_salary(self):
        da = self.salary * 0.20
        hra = self.salary * 0.15
        total_salary = self.salary + da + hra
        return total_salary

    def display(self):
        total = self.calculate_salary()
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Base Salary: ₹{self.salary}")
        print(f"Total Salary (with DA & HRA): ₹{total}")
        print("-" * 40)

emp1 = Employee("101", "Someone1", 50000)
emp2 = Employee("102", "Someone2", 65000)

emp1.display()
emp2.display()

#create a student class with: name, roll_no, marks (out of 100), create 3 student objects and display their objects. Add a method grade() that prints "pass" if marks>= 40, otherwise "fail"

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}"

    def grade(self):
        if self.marks >= 40:
            print(f"{self.name}: Pass")
        else:
            print(f"{self.name}: Fail")

student1 = Student("Student1", 101, 85)
student2 = Student("Student2", 102, 37)
student3 = Student("Student3", 103, 58)

print(student1)
print(student2)
print(student3)

student1.grade()
student2.grade()
student3.grade()
