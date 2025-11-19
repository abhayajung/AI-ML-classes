 # 1)Input two numbers form user and print their sum.

firstNum = int(input("Enter the first number"))
secondNum = int(input("Enter the second number"))
Sum = firstNum + secondNum
print(Sum)

# 2)WAP to input sides of square and print the area

length = int(input("Enter the side of a square:"))
Area = length**2
print(Area)

# 3)WAP to input 2 floating point numbers and print their average

Fn = float(input("Enter the first float number: "))
Sn = float(input("Enter the second float number: "))
Avr = (Fn+Sn)/2
print(Avr)

# 4)WAP to input 2 int numbers,a and b.print true if a>b or a=b .if not false

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a>=b:
    print(True)

else:
    print(False)

# 5)Ask the user for their age in year and convert them into months

Name = input("Enter your Name: ")
Age = int(input("Enter your age in years: "))
Months = Age*12
print(f"The age of Mr./Mrs. {Name} in years is entered to be {Age} year and the year converted to month is {Months} months. ")


