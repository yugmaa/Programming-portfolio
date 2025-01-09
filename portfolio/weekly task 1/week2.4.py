"""this program gives the number of sweets to be distributed to each pupil and counts the left over ones"""

student_number= int(input("enter number of students: "))
sweets_number= int(input("enter the number of sweets avialable: "))
distribution_number= int(sweets_number/student_number) #calcultaes the number of group formation possible
left_over= sweets_number%student_number #counts the number of left over student
print(f"{distribution_number} number of sweets will be given to each student and {left_over} number of sweets will be left over")