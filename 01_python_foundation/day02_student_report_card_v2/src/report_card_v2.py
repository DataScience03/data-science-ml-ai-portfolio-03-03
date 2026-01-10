
#student report card generator using list and loops 

'''
set the student Name
student class
marks
subjects

find the grade and percentage 
'''

name = input("enter a name: ")
class_name = input("enter a class: ")

subject = ["maths", "tamil", "enghlish"]
marks = []


for subjects in subject:
    mark = int(input(f"enter a {subjects} marks: " ))
    marks.append(mark)
    
    
total_mark = sum(marks)
average_mark = total_mark/len(subject)*100   
percentage = (total_mark/len(subject)*100)*100


if percentage >= 90:
    result= "A"
elif percentage >=70:
    result = "B"
elif percentage >= 60:
    result = "C"
else:
    result = "not disclosed"
    
    
print("\n======find percentage of students==========")

print("name:", name)
print("student_class: ", class_name) 
print("marks: ", marks)           
print("total marks:", total_mark)
print("avg mark:", average_mark)
print("percentage:", round(percentage,2))
print("Result: ", result)   
