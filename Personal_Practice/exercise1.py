# Question: Write a single line of code that sets can_vote to True if:
# (age is 18 or above) AND (citizenship is "Nepal") AND (not has_criminal_record).
# Print the value of can_vote.

age = int(input("Enter your age: "))
agemax = 18
citizenship = input("Enter you country: ")
citizenship_required = "Nepal"
has_criminal_record = input("Enter you have any criminal record: ")
criminal_record = "no"
can_vote = ((age>=agemax) and (citizenship==citizenship_required) and (has_criminal_record == criminal_record))
print(can_vote)