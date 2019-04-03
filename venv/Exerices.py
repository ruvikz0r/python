# Ex1: python program to print initials of a name

First = input("Enter your first name:")
Last = input("Enter your last name:")
greeting = "Hello there, %s %s"
print(greeting % (First, Last))

# Ex2: Types & Operators

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)
print("The numbers are equal")


