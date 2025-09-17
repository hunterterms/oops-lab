#1. wap to display the multiplication table
num1 = int(input("Enter a number: "))

print(f"Multiplication Table of {num1}")
for i in range(1, 11):
    print(f"{num1} x {i} = {num1 * i}")

#2. wap to print inverted pyramid of numbers
rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#3. wap to check if a input no. by the user is prime or not using a loop
num2 = int(input("Enter a number: "))

if num2 > 1:
    is_prime = True
    for i in range(2, num2):
        if num2 % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num2} is a prime number")
    else:
        print(f"{num2} is not a prime number")
else:
    print(f"{num2} is not a prime number")

#4. wap to calculate the sum of digits
num3 = int(input("Enter a number: "))