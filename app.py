# Single Console Program Using If-Else

print("Welcome to Simple Python Programming")

# Take user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
number = int(input("Enter a number to check even/odd: "))

print("\nHello", name)

# Check voting eligibility
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Check pass or fail
if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

# Check even or odd
if number % 2 == 0:
    print("The number is Even Number.")
else:
    print("The number is Odd Number.")
