#WAP to 

number = int(input("Enter a number of num you wish to make the sum out of:  "))
count = 1
sum = 0
while count<=number:
    num = int(input(f"Enter {count}st number:  "))
    sum = sum + num
    count+=1
    print(sum)

