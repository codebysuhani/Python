#Create student class that takes name and marks of 3 subjects as arguments in constructor.then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

        def get_avg(self):
            sum = 0
            for val in self.marks:
                sum += val
                
            print("hi", self.name, "your avg score is:", sum/3)


s1 = Student("Suhani", [88,90,85])
s1.get_avg()

s2 = Student("Aarti", [86,98,60])
s2.get_avg()

s3 = Student("Devyani", [91,80,75])
s3.get_avg()