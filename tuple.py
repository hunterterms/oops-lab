# 1. wap to convert a tuple into a list and add a new element
tup = (1, 2, 3)
lst = list(tup)
lst.append(4)
print("Updated list:", lst)

# 2. wap to input a tuple of numbers and print only the prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = tuple(map(int, input("Enter numbers separated by space: ").split()))
print("Prime numbers in tuple:", [n for n in nums if is_prime(n)])

# 3. wap to check whether a given element exists in a tuple or not
tup = (10, 20, 30, 40)
element = int(input("Enter element to search: "))

if element in tup:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

# 4. wap to swap the values of two variables using a tuple
a = 5
b = 10
print("Before swap:", a, b)

# Swapping using tuple unpacking
a, b = b, a
print("After swap:", a, b)

# 5. wap to count how many times a particular element appears in a tuple using loop
tup = (1, 2, 3, 2, 4, 2, 5)
element = int(input("Enter element to count: "))

count = 0
for item in tup:
    if item == element:
        count += 1

print(f"{element} appears {count} times in the tuple.")