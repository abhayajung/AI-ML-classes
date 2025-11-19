# password check game task

password=input("Enter your password:")
min_len=12
password_len=len(password)
if password_len<=min_len:
    print("Valid password length")
else:
    print("Invalid password length")

# a=6787648
# b=88643
# print(a>b)

# a=12989
# b=7656
# a*=12
# b/=126
# print(a,b)

# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# print(f"Sum is {a+b}\nSubtract is {a-b}\nMultiply is {a*b}\nDivide is {a/b}")

# quantity=int(input("Enter the quantity:"))
# price=float(input("Enter the price per piece:"))
# discount=int(input("Enter the discount rate:"))
# tax=int(input("Enter the tax rate:"))
# total=quantity*price
# discount_amount=(discount/100)*total
# tax_amount=(tax/100)*total
# print(f"The amount to be paid after {discount}% discount and {tax}% tax is {(total-discount_amount+tax_amount)}")