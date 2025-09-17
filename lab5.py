#1. a school maintains students' grade in 3 subjects. waf that returns the average marks, show how default parameters could be used if a student has missed a test (missing mark to be 0)
def averageMarks(mark1=0, mark2=0, mark3=0):
    total = mark1 + mark2 + mark3
    return total / 3

print("average marks: ", averageMarks(85, 90))
print("average marks: ", averageMarks(70, 80, 90))

#2. a cafe allows the customer to order multiple items. waf totalBill *  items where each item is given as a tuple (name, price). this function should return the total bill
def totalBill(*items):
    total = 0
    for item in items:
        total += item[1]
    return total

print("total price: ", totalBill(("bread", 40), ("tea", 90)))

#3. in an ecommerce system, applyDiscount with parameteres(price, discount) is frequently used. management asked to use repetitive function definitions 
applyDiscount = lambda price, discount: price - discount

print("total price after discount: ", applyDiscount(1000, 100))
print("total prcie after discount: ", applyDiscount(750, 200))

#4. waf which calculates area, if both length and breadth are provided return rectangle's area, if only length is provided return square's area
def calculateArea(length, breadth=None):
    if breadth is None:
        return length ** 2
    else:
        return length * breadth

print(calculateArea(4))
print(calculateArea(5, 3))

#5. waf, Bonus with parameters (salary, rate=0.01) that calculates the new salary after applying a bonus rate, call the function once using positional argument and once using keyword argument, show a  case where incorrect mixing of positonal and keyword argument shows an error
def Bonus(salary, rate=0.01):
    return salary + (salary * rate)

print(Bonus(50000))
print(Bonus(50000, 0.05))
print(Bonus(50000, rate=0.05))
# print(Bonus(rate=0.05, 50000)) error

#6. design a function, studentRecord with parameters, course, * subjects, ** details, that stores the course name, store multiple keyword using the * arguments, that store data like name, age, rate using keyword arguments. wap that demostrate all three cases in one function call
def studentRecord(course, *subjects, **details):
    print(f"Course: {course}")
    print(f"Subjects: {', '.join(subjects)}")
    
    for key, value in details.items():  
        print(f"{key.capitalize()}: {value}")

studentRecord("cse", "maths", "coa", "dsa", name="Anay Sahu", age=18, rate=0.1)