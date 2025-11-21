#if,elif,else and nested if

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if (a>b) and (a>c):
    print(f"{a} is greatest among {b} and {c}")
elif (b>c):
    print(f"{b} is greatest among {a} and {c}")
else:
    print(f"{c} is greatest among {a} and {b}")


a=int(input("Enter the first number:"))
if a>=1000:
    if a%10==0:
        print(f"{a} is greater than 1000 and divisible by 10.")
    else:
        print(f"{a} is greater than 1000 and  not divisible by 10.")
else:
    print(f"{a} is less than 1000.")


mark=int(input("Enter the first number:"))
if mark>=40:
    if mark>=50 and mark<70:
        print(f"")  


# name=input("Enter your name:")
# max=int(input("Enter how many times to print your name:"))
# count=0
# while count<max:
#     print(name)
#     count+=1


# name = str(input('Enter your name: '))
# counts = int(input("Enter the number of turns you want to repaet your name: "))
# count = 0
# while(count<counts):
#     print(f"{count+1} {name}")
#     count = count+1

# count = 90
# while (count>counts):
#     print(name)
#     count-=1




# # name=input("Enter your name:")
# start = int(input("Enter the start of the loop: "))
# stop=int(input("Enter how many times to print your name:"))
# step = int(input("Enter how many terms you want to skip: "))
# # for i in range(start,stop,step):
# #     print(name)

start = int(input("Enter the start of the loop: "))
stop=int(input("Enter how many times to print your name:"))
step = int(input("Enter how many terms you want to skip: "))
for i in range(start,stop,step):
    print(i)


for i in range(0,100,2):
    if i>20:
        break
    print(i)
  

for i in range(0,100,2):
    if i>20 and i<80:
        continue
    print(i)