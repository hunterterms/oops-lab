# 1. wap to input 10 int in the list and print the largest and the smallest number
nums = []
for i in range(10):
    val = int(input(f"Enter integer {i+1}: "))
    nums.append(val)

largest = max(nums)
smallest = min(nums)

print("Numbers: ", nums)
print("Largest number: ", largest)
print("Smallest number: ", smallest)

# 2. wap to input 5 names in a list and print them in sorted order
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

names.sort()
print("Sorted names: ", names)

# 3. wap to reverse a list without using the reverse function
my_list = [10, 20, 30, 40, 50]
reversed_list = my_list[::-1]

print("Original list: ", my_list)
print("Reversed list: ", reversed_list)

# 4. given a list of marks, wap to find the avg of marks and display students who score above the avg
marks = []
n = int(input("Enter number of students: "))

for i in range(n):
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

avg = sum(marks) / n
print("Average marks: ", avg)

print("Students scoring above average: ")
for i in range(n):
    if marks[i] > avg:
        print(f"Student {i+1} → {marks[i]}")

# 5. wap to print all the items of a list using while loop by going through all the index numbers
items = ["apple", "banana", "cherry", "date"]
i = 0

while i < len(items):
    print(f"Index {i} → {items[i]}")
    i += 1