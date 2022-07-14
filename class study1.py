
# A class named SS3C and object named student.

class SS3C:

# defined __init__ function for object attributes.

    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

# defined function for object method(functionalities).

    def my_func(self):
        print(self.name + " is a " + self.sex + " who is", self.age,"years old")

student = SS3C("Arinze","male",30)
student.my_func()






