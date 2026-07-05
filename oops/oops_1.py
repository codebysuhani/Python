class Student:

    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in database..")

s1 = Student("suhani")
print(s1.name)

s2 = Student("aman")
print(s2.name)