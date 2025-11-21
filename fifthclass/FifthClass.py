#IF,ELIF and ELSE statement

number=int(input("Enter the number:"))
if number%2==0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
print("The number is checked successfully!!")


name=input("Enter your name:")
if name!="":#if name is not equal to blank
    print(f"Hello! {name}, How are you?")
if len(name) != 0:
    print(f"hello! {name} how are you?")


discount_rate=10/100
total_amount=float(input("Enter the total amount:"))
if total_amount>=1000:
    print(f"The total amount to be paid is {total_amount-(total_amount*discount_rate)}")
else:
    print("Thank you for shopping")





num=int(input("Enter any number:"))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")


num1=int(input("Enter any number:"))
num2=int(input("Enter any number:"))
num3=int(input("Enter any number:"))
if num1>num2 and num1>num3:
    print(f"{num1} is greatest among {num2} and {num3}")
elif num2>num3:
    print(f"{num2} is greatest among {num1} and {num3}")
else:
    print(f"{num3} is greatest among {num1} and {num2}")