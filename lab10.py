#design a python program for a univ system to manage student grades and evaluation, demostrating polymorphism: 
#1. method overriding: create a base class 'person' with a method get_role, create derived classes "student" and "class" that override get_role.
#2. method overloading: create a class "grade" with a method "calculate", using default argument to handle single or multiple marks.
#3. operator overloading: create a class "score" with attribute marks, overload the plus operator using add to sum two score objects.
#4. create objects and demostrate all types of polymorphism

# 1. METHOD OVERRIDING
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_role(self):
        return "Generic Person"
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Role: {self.get_role()}")

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major
    
    def get_role(self):
        return f"Student in {self.major}"
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

class Teacher(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department
    
    def get_role(self):
        return f"Teacher in {self.department} Department"
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")


# 2. METHOD OVERLOADING
class Grade:
    def __init__(self, course_name):
        self.course_name = course_name

    def calculate(self, mark1, mark2=None, mark3=None, mark4=None):
        """
        Calculate average for single or multiple marks
        - If only mark1 provided: returns mark1
        - If multiple marks provided: returns average
        """
        marks = [mark1]
        
        if mark2 is not None:
            marks.append(mark2)
        if mark3 is not None:
            marks.append(mark3)
        if mark4 is not None:
            marks.append(mark4)
        
        average = sum(marks) / len(marks)
        return average
    
    def display_grade(self, average):
        print(f"\nCourse: {self.course_name}")
        print(f"Average Score: {average:.2f}")

        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        print(f"Letter Grade: {grade}")
        return grade


# 3. OPERATOR OVERLOADING
class Score:
    def __init__(self, marks, course=""):
        self.marks = marks
        self.course = course
    
    def __add__(self, other):
        """Overload + operator to sum marks of two Score objects"""
        total_marks = self.marks + other.marks
        combined_course = f"{self.course} + {other.course}"
        return Score(total_marks, combined_course)
    
    def __str__(self):
        """String representation of Score object"""
        return f"Score(Course: {self.course}, Marks: {self.marks})"
    
    def __repr__(self):
        return self.__str__()


# 4. DEMONSTRATION OF ALL POLYMORPHISM TYPES
def main():
    print("=" * 70)
    print("UNIVERSITY GRADE MANAGEMENT SYSTEM - POLYMORPHISM DEMONSTRATION")
    print("=" * 70)

    # 1. DEMONSTRATING METHOD OVERRIDING
    print("\n1. METHOD OVERRIDING DEMONSTRATION")
    print("-" * 70)

    person = Person("John Doe", 30)

    student = Student("Alice Johnson", 20, "STU12345", "Computer Science")

    teacher = Teacher("Dr. Robert Smith", 45, "EMP67890", "Mathematics")

    print("\nBase class Person:")
    person.display_info()
    
    print("\nDerived class Student:")
    student.display_info()
    
    print("\nDerived class Teacher:")
    teacher.display_info()

    print("\n\nPolymorphic behavior with list of Person objects:")
    people = [person, student, teacher]
    for p in people:
        print(f"  {p.name}: {p.get_role()}")

    # 2. DEMONSTRATING METHOD OVERLOADING
    print("\n\n2. METHOD OVERLOADING DEMONSTRATION")
    print("-" * 70)

    math_grade = Grade("Mathematics")
    cs_grade = Grade("Computer Science")
    physics_grade = Grade("Physics")

    print("\nCalculating grade with single mark:")
    single_mark_avg = math_grade.calculate(85)
    math_grade.display_grade(single_mark_avg)
    
    print("\nCalculating grade with two marks:")
    two_marks_avg = cs_grade.calculate(88, 92)
    cs_grade.display_grade(two_marks_avg)
    
    print("\nCalculating grade with four marks:")
    four_marks_avg = physics_grade.calculate(75, 82, 90, 88)
    physics_grade.display_grade(four_marks_avg)
    
    # 3. DEMONSTRATING OPERATOR OVERLOADING
    print("\n\n3. OPERATOR OVERLOADING DEMONSTRATION")
    print("-" * 70)

    score1 = Score(85, "Midterm Exam")
    score2 = Score(92, "Final Exam")
    score3 = Score(78, "Project")
    
    print("\nOriginal Score objects:")
    print(f"  Score 1: {score1}")
    print(f"  Score 2: {score2}")
    print(f"  Score 3: {score3}")

    print("\nUsing overloaded + operator:")
    total_score_1_2 = score1 + score2
    print(f"  score1 + score2 = {total_score_1_2}")

    total_all_scores = score1 + score2 + score3
    print(f"  score1 + score2 + score3 = {total_all_scores}")

    print(f"\n  Total Marks: {total_all_scores.marks}")
    print(f"  Average: {total_all_scores.marks / 3:.2f}")
    
    # COMPLETE EXAMPLE: Student Evaluation
    print("\n\n" + "=" * 70)
    print("COMPLETE STUDENT EVALUATION EXAMPLE")
    print("=" * 70)

    eval_student = Student("Emma Watson", 21, "STU54321", "Data Science")
    print("\nStudent Information:")
    eval_student.display_info()

    print("\n\nCourse Grades:")
    courses = {
        "Database Systems": [88, 90, 85, 92],
        "Machine Learning": [95, 93],
        "Software Engineering": [87, 89, 91]
    }
    
    all_scores = []
    for course_name, marks in courses.items():
        grade_obj = Grade(course_name)
        avg = grade_obj.calculate(*marks)
        grade_obj.display_grade(avg)
        all_scores.append(Score(avg, course_name))

    print("\n\nOverall Performance (using operator overloading):")
    total_score = all_scores[0]
    for score in all_scores[1:]:
        total_score = total_score + score
    
    overall_avg = total_score.marks / len(all_scores)
    print(f"Overall Average: {overall_avg:.2f}")
    
    if overall_avg >= 90:
        print("Overall Grade: A (Excellent)")
    elif overall_avg >= 80:
        print("Overall Grade: B (Very Good)")
    elif overall_avg >= 70:
        print("Overall Grade: C (Good)")
    else:
        print("Overall Grade: D (Needs Improvement)")
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
