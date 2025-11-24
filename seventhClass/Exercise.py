#Create a list and a set with five fruits 
#Display the first and last fruit

fruit_list = ["apple", "mango", "tomato", "banana", "milk"]
set = {"apple", "mango", "tomato", "banana", "milk"} 
print(fruit_list[0:4:3])
# print(set[0])

# Create a dictionary with 3 students and their marks.Print all names and their marks

student_marks={
    "Abhaya":"20",
    "Prakash":"90",
    "Prasan":"100"
}
for i,j in student_marks.items():
    print(f"{i}={j}")

