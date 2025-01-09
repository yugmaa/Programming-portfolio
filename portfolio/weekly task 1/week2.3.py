"""this program promts user to give number of students and group size and displays the number of groups needs and the number of students who will be left over in a smaller group."""

student_number= int(input("How many students?"))
group_size= int(input("Required group size?"))
group_number= int(student_number/group_size) #number of groups possible
left_over= student_number%group_size #left over students
# checks grammar
if left_over<=1:
    print(f"There will be {group_number} groups with {left_over} student left over.") 
else:   
    print(f"There will be {group_number} groups with {left_over} students left over.")
