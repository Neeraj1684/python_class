marks_dict = { 'Prasad' : 90,
'Neeraj' : 95, 
' Shaurya' : 85,
'omkar' : 84,
'ajay' : 10
}
max_val = 0

for student, mark in marks_dict.items():
  if mark > max_val :
    max_val = mark
    max_student = student
  
print(max_student)


#output
#Neeraj
