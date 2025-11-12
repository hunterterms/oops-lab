# A university wants to develop a small Python program for Student Result Processing
# program should:
# a) Take input of marks obtained and total marks.
# b) Calculate the percentage of the student.
# c) Handle possible exceptions like:
# o ValueError: When non-numeric input is given.
# o ZeroDivisionError: When the total marks entered is zero.
# o FileNotFoundError: When the result file to store data is missing.
# o Generic Exception: To handle any other unexpected errors.
def student_result_processing():
    try:
        marks_obtained = float(input("Enter marks obtained: "))
        total_marks = float(input("Enter total marks: "))

        percentage = (marks_obtained / total_marks) * 100
        print(f"Percentage: {percentage:.2f}%")

        filename = "student_result.txt"
        with open(filename, "w") as file:
            file.write(f"Marks Obtained: {marks_obtained}\n")
            file.write(f"Total Marks: {total_marks}\n")
            file.write(f"Percentage: {percentage:.2f}%\n")
        print(f"Result saved successfully in '{filename}'")

    except ValueError:
        print("Error: Please enter numeric values for marks.")
    except ZeroDivisionError:
        print("Error: Total marks cannot be zero.")
    except FileNotFoundError:
        print("Error: The result file could not be found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

student_result_processing()

# Write a Python program that:
# * Takes input for basic salary, HRA, and DA.
# * Calculates the gross salary (gross = basic + HRA + DA).
# * Handles exceptions:
#    - ValueError: If the user enters a non-numeric value.
#    - TypeError: If an unsupported data type is used in calculation.
#    - KeyboardInterrupt: If the user interrupts input using Ctrl+C.
#    - Generic Exception: To handle any other unknown errors.
def employee_salary_calculation():
    try:
        basic = float(input("Enter Basic Salary: "))
        hra = float(input("Enter HRA: "))
        da = float(input("Enter DA: "))

        gross = basic + hra + da
        print(f"Gross Salary = {gross:.2f}")

    except ValueError:
        print("Error: Please enter numeric values only.")
    except TypeError:
        print("Error: Unsupported data type used in calculation.")
    except KeyboardInterrupt:
        print("\nInput interrupted by user (Ctrl+C).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

employee_salary_calculation()

# Write a Python program that:
# * Takes a list of integers and an index number from the user.
# * Prints the element present at that index.
# * Handles exceptions:
#    - IndexError: If the index is out of range.
#    - ValueError: If a non-integer index is entered.
#    - TypeError: If the list contains incompatible data types.
#    - Generic Exception: For any other error.
def list_element_access():
    try:
        user_input = input("Enter integers separated by spaces: ")
        numbers = list(map(int, user_input.split()))

        index = int(input("Enter index to access: "))

        print(f"Element at index {index}: {numbers[index]}")

    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter valid integers only.")
    except TypeError:
        print("Error: Incompatible data type in list.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

list_element_access()
