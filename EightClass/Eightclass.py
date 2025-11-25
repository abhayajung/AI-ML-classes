# Basic understanding of functions

def func1():#function definition
    # function implementation here
    print("hello python programmer")
func1()


 
#parameters in function
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

def sum(a,b):
    print(f"sum is {a+b}")
    print(f"product is {a*b}")
    
#funtion call
sum(a,b)
sum(a,b)
sum(a,b)
sum(a,b)

def func2(name,age):   # parameters passing  
    print(f"hello {name}")
    print(f"you are {age} years old")

func2("ram",30)   #argument passing


def func2(name,age):   # parameters passing
    print(f"hello {name}")
    print(f"you are {age} years old")

func2("ram",30)   #argument passing
func2("shyam",40)


a = int(input("Enter a number"))
b = int(input("Enter a number"))
name = input ("enter a name")


def sum(a,b):
    print(f"sum is {a+b}")
    print(f"product is {a*b}")
    print(f"{name} is greatest")
     
     
sum(a,b)
sum(a,b)



# Return statement

def sum_number(num1,num2):
    return num1 + num2

sum_number(23,45)
print(sum_number(23,45))

sum_result = sum_number(23,45)
print(sum_result)

# WAP to perform sum,difference, product and division using single return statement and store the value back to their corresaponding variables : sum,difference,product and division


def calculate(num1,num2):
    return num1 +  num2, num1 - num2 , num1*num2 , num1/num2
  
result = calculate(5,3)
print(result)

sum, difference , product , division = result
print(f"Sum: {sum}")
print(f"product : {product}")
print(f"difference : {difference}")
print(f"division : {division}")




# def fun2(name,age):   #name,age are parameters
#     print(f"Hello {name}")
#     print(f"You are {age} years old")
# fun2("Krishna",30)  #argument passing



# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# def sum(a,b):
#     print(f"Sum is {a+b}")
# sum(a,b)


# Create a multiple function for addition, subtraction, 
# multiplication and division and ask the user to perform 
# which operation to be done and do the task as per user input

# def addition(a,b):
#     print(f"Addition is {a+b}")
# def subtraction(a,b):
#     print(f"Subtraction is {a-b}")
# def multiplication(a,b):
#     print(f"Multiplication is {a*b}")
# def division(a,b):
#     print(f"Division is {a/b}")
# a = input("Enter which operation should be done:")



# def sum_number(a,b):
#     return a+b
# # print(sum_number(23,45))
# sum_result=sum_number(23,45)
# print(sum_result)


# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# def sum(a,b):
#     return a+b
# def difference(a,b):
#     return a-b
# def product(a,b):
#     return a*b
# def division(a,b):
#     return a/b
# sum=sum(a,b)
# difference=difference(a,b)
# product=product(a,b)
# division=division(a,b)

def calculate(a,b):
    return a+b,a-b,a*b,a/b
result=calculate(5,2)
sum,difference,product,division=result
print(f"Sum is {sum}\nDifference is {difference}\nProduct is {product}\nDivision is {division}")