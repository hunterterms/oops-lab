import sys

#1. dist. b/w two points with user user input
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
print("Distance between them is: ", b-a)

#2. take two num as command line args and print their sum
#c = int(sys.argv[1])
#d = int(sys.argv[2])
#print("The sum is: ", c+d)

#3. reverse a string
string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string: ", reversed_string)

#4. no. of vowels
e = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0 

for char in e:
    if char in vowels:
        count += 1
print("Number of vowels: ", count)

#5. palindrome
f = input ("Enter a string: ")
if f == f[::-1]:
    print("It is a paindrome.")
else:
    print("It is not a palindrome.")

#6. replace all spaces in a sentance with hyphens
sentence = input("enter a sentence: ")
new = sentence.replace(" ","-")
print("Updated sentence: ", new)

#7. convert the first letter of each word to uppercase
g = input("Enter a sentence:")
capital = g.title()
print("Updated sentence:", capital)