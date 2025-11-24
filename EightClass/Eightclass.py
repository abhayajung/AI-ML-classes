basic understanding of the function

# def func1():
    # code implementation here
#     print("hello python programmer")

# func1()


 
#parameters in function
# a = int(input("Enter a number"))
# b = int(input("Enter a number"))

# def sum(a,b):
#     print(f"sum is {a+b}")
#     print(f"product is {a*b}")
    
    


# sum(a,b)
# sum(a,b)
# sum(a,b)
# sum(a,b)

# def func2(name,age):   # parameters passing  
#     print(f"hello {name}")
#     print(f"you are {age} years old")

# func2("ram",30)   #argument passing


# def func2(name,age):   # parameters passing
#     print(f"hello {name}")
#     print(f"you are {age} years old")

# func2("ram",30)   #argument passing
# func2("shyam",40)


# a = int(input("Enter a number"))
# b = int(input("Enter a number"))
# name = input ("enter a name")


# def sum(a,b):
#     print(f"sum is {a+b}")
#     print(f"product is {a*b}")
#     print(f"{name} is greatest")
     
     
# sum(a,b)
# sum(a,b)



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