#BREAK AND CONTINUE#

for i in range(10,24):
    if i == 15:
        # break
        continue
    print(i)

# To print the even number between 10 and 20#
for i in range(10,21):
    if(i%2)!=0:
        continue
    print(i)

#PASS STATEMENT#

for i in range(10,20):
    pass #used to skip the execution block to be implemented in a statement for the time being and can be changed later
print("hello world")


#STRINGS#

#Collection of characters "",'',""" """#
name = 'abhaya jung khadka'
print(type(name))
name = "this is abhaya"
name = '''
this
is
name
'''
print(name)
print(type(name))

#INDEXING# 
s1 = "python program"
#start from 0 positively and start from -1 negatively
print(s1[5])
print(s1[6])
print(s1[-6])


#SLICING OPERATOIN#
# to extract  the desired subtracting from the string
#String[start:end:step]
s1 = "python program"
s2 = s1[7:14:-2]
print(s2)

s3 = s1[-7::2]
print(s3)

s4 = "This is string"
s5 = s4[6:12]
print(s5)

#METHODS#

print(s4.count('i'))
print(s4.upper())
print(s4.lower())

for i in s4:
    print(i)

#DATA STRUCTURES#

#LIST#

list1 = [1,2,3,4]
print(type(list1))

#list is a collection of elements
#list can be collection of mixed datatypes whereas arrays are defined as the collection of similar datatypes.

list2 = [1,89,"hello",'pythom']
print(list2)

list1 =[]
print(list1)

#to add the element in the list
#append() method
list1.append(23)
print(list1)
list2 = [12,34,56,67]
#list is mutable
#removable
#addable
list2[2] = 190#mutable
print(list2)
list2.append(45)#addable
print(list2)
# list2.insert(index, value)
list2.insert(2,90)#addable at designated location
print(list2)

#extend
list2.extend([34, 45, 56, 67])
# print(list2)

list2 = [12,45,67,89,56,2]
list2.sort()#arranges in ascending order
list2.sort(reverse=True)#arranges in descending order
print(list2)


# write a program to ask the marks of physics of 5 student and append that marks in the list

physics_marks = []
count = 0

while count < 5:
    mark = float(input("Enter the marks: "))
    physics_marks.append(mark)
    count = count+1
print(physics_marks)

#Explore all the remaining methods

#TUPLE#

#tuple is IMMUTABLE

tuple_1 = (1,6,5,7,3,1,3,42,6,7,1)#value change garna sakkina
print(type(tuple_1))

tuple_1[2] = 16
print(tuple_1)#not possible


tuple_1.append(34)
print(tuple_1)

print(tuple_1[0])

print(tuple_1.count(1))

# packing and unpakcing tuple

# unpacking 
# my_tuple = (45,56,78)
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

#packing
# a=56
# b=78
# c=78

# my_tuple = a, b, c
# print(my_tuple)

# Concatenation in tuple
# tuple_1 = (3,4,5,6)
# tuple2 = (45,67,89,23)
# print(tuple_1 + tuple2)


#SET

# set1 = {}#not possible
# set1 = set()
# print(type(set1))

# set1 = {1,3,5,6,4}
# print(set1)
# print(type(set1))

# list1=[23,23,45,67,89]
# tuple1=(23,23,45,67,89)
# set1={23,23,45,67,89}#duplicate value not possible
# print(list1)
# print(tuple1)
# print(set1)#indexing not possible

set1 = {1, 3, 4 , 5}
# set2 = {2, 4, 5, 6}

# #union
# set3 = set1.union(set2)
# print(set3)
# set4 = set1.intersection(set2)
# print(set4)


# difference

#to add the element in the set

# set1.add(45)
# print(set1)

# set1.remove(45)
# print(set1)

# set2 = {23,45,67}
# set2.discard(100)
# # set2.remove(100)
# print(set2)


#DICTIONARY

# dict1 = {}
# print(type(dict1))

# data are structured in key value pair
# key = value
#dixtionary book -> word and its corresponding meaning

# dict1 = {
#     "Name" : "Sayapatri Group",
#     "Adress" : "Biratnagar",
#     "Work" : "IT company"
# }
# print(dict1)

# print(dict1["Name"])
# print(dict1["Adress"])

# #methods

# # print(dict1.keys())
# # print(dict1.values())
# # print(dict1.items())

# # nested dixtionary
# #dictionary inside dictionary
# student = {
#     "student1":{
#         "Name":"Name of student1",
#         "section":"sun",
#         "roll":"345",
#         "marks":[34,56,77]
#     },
#     "student2":{
#         "Name":"Name of student2",
#         "section":"moon",
#         "roll":"567",
#         "marks":[34,56,77]
#     },
#     "student3":{
#         "Name":"Name of student23",
#         "section":"moon",
#         "roll":"567",
#         "marks":[34,56,77]
#     },

# }
# print(student)


student = {
    "Name":"something",
    "section":"jvns",#Keys should be unique
    "roll":"567",
    "mmarks":[56,8,9],
    
}
# print(student)

# # iterate through the keys

# for i in student.keys():
#     print(i)

# itertion throguh values
# for i in student.values():
#     print(i)

#iterate through key values pair

# for i,j in student.items():
#     print(f"{i}={j}")

# print(student)

# TO update the value of the key

# student["section"] = "moon"
# print(student)

# student.update({"section":"star"})
# print(student)






































#excalidraw.com