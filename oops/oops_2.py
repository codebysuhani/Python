class Student:

    college_name = "ABC college"
    name = "anonymous"

    #default constructors
    def __init__(self):
        pass

    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")


s1 = Student("suhani", 97)
print(s1.name, s1.marks)

s2 = Student("aman", 99)
print(s2.name, s2.marks)

print(Student.college_name)



