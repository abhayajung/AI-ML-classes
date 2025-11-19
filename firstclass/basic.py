print("Name=Abhaya jung khadka\nRoll=813045")
name="Prakash Shah"
print(name.replace("Abhaya","Prakash").replace("Jung khadka","shah"))


print("Abhaya jung khadka 813045\n"*8)
print("""
      Name:Abhaya jung khadka
      Roll no:813045
      """*3)

name="Abhaya jung khadka"
print(name)

name=input("Enter your name:")
print(f"Good morning {name} How are you?")

a=43
b=23
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)


a=b=c=50
print(a,b,c)

a=12; b=34 ;c=13
print(a,b,c)

a,b,c=12,23,14
print(a,b,c)

# swapping operations 
a,b=12,13
a,b=b,a
print(a,b)


fn,ln="abhaya","jung khadka"
fn,ln=ln,fn
print(fn,ln)


# Data Types
a=50      #integer
b=1.66387   #float
c="Prakash"   #string
d=True   #boolean
e=2+3j   #complex
print(type(a),type(b),type(c),type(d),type(e))


# type casting
a="345"
print(type(a))
b=int(a)
print(type(b))

name="Abhaya jung khadka"
print(type(name))
name2=int(name)
print(type(name2))



name=input("Enter your name:")
print(f"Your name is {name}")

a=int(input("Enter first number:"))
b=int(input("Enter first number:"))
print((a+b)/2)


# operators

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(f"Add of {a} and {b} is",a+b)
print(f"Subtract of {a} and {b} is",a-b)
print(f"Multiply of {a} and {b} is",a*b)
print(f"Division of {a} and {b} is",a/b)
print(f"Modulus of {a} and {b} is",a%b)
print(f"Exponential of {a} and {b} is",a**b)
print(f"Floor division of {a} and {b} is",a//b)




# logical operators
print(f"The sum of 5 and 6 is {5+6}")

#And truth table
print("And truth table")
print(f"True and True :{True and True}")
print(f"True and False :{True and False}")
print(f"False and True :{False and True}")
print(f"False and False :{False and False}")

#Or truth table
print("Or truth table")
print(f"True or True :{True or True}")
print(f"True or False :{True or False}")
print(f"False or True :{False or True}")
print(f"False or False :{False or False}")

#Not truth table
print("Not truth table")
print(f"not True :{not True}")
print(f"not False :{ not False}")