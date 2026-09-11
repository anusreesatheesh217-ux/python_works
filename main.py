# A.Python is an indent based programming language
teams = ['Data', 'AI', 'DevOps']
for t in teams:
     print('Hello', t, 'Team from Inceptez Technologies')
     print('Keep Learning and Exploring!')

# B. Commented line in Python
# Number of students
students = 100

# Number of trainers
trainers = 2

'''
This program calculates the total number
of students and trainers.
'''
total = students + trainers
print(total)

# Dead Code
# print("Welcome to Inceptez Python Learning")
# Re-activated Code
print("Welcome to Inceptez Python Learning")

# C. Playing with Quotes
msg1 = "This is Inceptez's \"Python\" class for Data Engineers & AI Engineers"
print(msg1)

msg2 = 'This is Inceptez\'s "Python" class for Data Engineers & AI Engineers'
print(msg2)

msg3 = '''This is Inceptez's "Python" class for Data Engineers & AI Engineers'''
print(msg3)

message = '''
Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey.
'''
print(message)

# D.Let's learn all about VARIABLES
# Use Case 1: Store student details using variables

# Student Name
student_name = "Anu"

# Course Name
course_name = "Python Fundamentals"

# Training Institute Name
institute_name = "Inceptez Technologies"

# Print the formatted message
print("Name:", student_name, "is learning the course", course_name, "at the institute", institute_name)

# Use Case 2: Demonstrate Dynamic Inference

# Fee amount
fee = 45000

# Python automatically identifies the datatype
print("Fee datatype:", type(fee))

# Use Case 2: Demonstrate Dynamic Typing

# Fee amount
fee = 45000

# Adding 18% GST
fee = fee + (fee * 0.18)

# Display fee after GST
print("Fee after GST:", fee)

# Datatype changed from int to float
print("Fee datatype after GST:", type(fee))

# Use Case 2: Demonstrate Strong Typing

# Fee amount (integer)
fee = 45000

# GST description (string)
gst = "Eighteen percent"

# Python does not allow adding number and string
#print(fee + gst)

# E.Variables Naming Conventions
# Use Case 1: Identify invalid variable names

# Invalid - starts with a number
# 2student = "Ravi"

# Valid - starts with underscore
_student_id = 1001

# Valid - starts with a letter
studentName = "Priya"

# Invalid - contains space
# class name = "Python"

# Valid - uses underscore
inceptez_batch = "Morning"

# Print valid variables
print(_student_id)
print(studentName)
print(inceptez_batch)

# Use Case 2: Demonstrate different naming conventions

# PascalCase
DataEngineeringBatch = "Batch A"

# camelCase
dataEngineeringBatch = "Batch B"

# snake_case
data_engineering_batch = "Batch C"

# Print all variables
print("PascalCase:", DataEngineeringBatch)
print("camelCase:", dataEngineeringBatch)
print("snake_case:", data_engineering_batch)

# F. Type identification & Casting

# Use Case 1: Type Identification and Casting

# Get employee age from user
age = input("Enter employee's age: ")

# Check datatype before conversion
print("Datatype before conversion:", type(age))

# Convert string to integer
age = int(age)

# Retirement age
retirement_age = 60

# Calculate years left for retirement
years_left = retirement_age - age

# Display result
print("You will retire in", years_left, "years at Inceptez Technologies")

# Use Case 2: Fix Type Error using Type Casting
salary = "50000"
bonus = 10000

# Convert salary from string to integer
salary = int(salary)

# Add salary and bonus
total_salary = salary + bonus

# Display result
print("Total Salary in Inceptez:", total_salary)

#G. Data types and casting
# Use Case 1: Employee Salary Breakdown

# Get employee details from user

employee_name = input("Enter employee name: ")

base_salary = float(input("Enter base salary: "))

hra_percent = int(input("Enter HRA percentage: "))

bonus_amount = float(input("Enter bonus amount: "))

# Calculate HRA

hra = base_salary * (hra_percent / 100)

# Calculate Total Salary

total_salary = base_salary + hra + bonus_amount

# Display salary details

print("\nEmployee:", employee_name)

print("Base Salary:", base_salary)

print("HRA @", hra_percent, "%:", hra)

print("Bonus:", bonus_amount)

print("Total Salary Payable: ₹", total_salary)

# Use Case 2: Student Result Classification

# Get marks from user

marks = input("Enter marks: ")

try:

    # Convert string to float

    marks = float(marks)

    # Classification

    if marks >= 90:
        print("Outstanding")

    elif marks >= 75:
        print("Excellent")

    elif marks >= 50:
        print("Pass")

    else:
        print("Fail")

except:

    print("Invalid marks entered — Please provide numeric input.")

# Use Case 3: Fix datatype mismatch

# Get product details

    item_name = input("Enter product name: ")

    price = float(input("Enter price per item: "))

    quantity = int(input("Enter quantity: "))

    # Calculate total cost

    total_cost = price * quantity

    # Display result

    print("You purchased", quantity, "units of", item_name)

    print("Total payable:", total_cost, "INR")