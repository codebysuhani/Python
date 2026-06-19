#grade students based on marks
marks = int(input("Enter student marks:"))

if(marks >= 90):
    print('grade = "A"')
elif(marks < 90 and marks >= 80):
    print('grade = "B"')
elif(marks < 80 and marks >= 70):
    print('grade = "C"')
else:
    print('grade = "D"')