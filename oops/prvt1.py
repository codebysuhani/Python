class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome()) #work
print(p1.__name) #not work
print(p1.__hello) #not work
