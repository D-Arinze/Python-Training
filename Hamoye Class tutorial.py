# Class tutorial on Hamoye

class Car:

# defined attributes of the object.

    def __init__(self,model,color,bodytype,speed):
        self.model = model
        self.color = color
        self.bodytype = bodytype
        self.speed = speed

# defined function for object method1

    def my_func(self):
        print("The model of my car is a " + self.model + " which is " + self.color + " in color and is a " + self.bodytype + " and very " + self.speed)

# defined function for object method2

    def diff_model(self,model):
        self.model = model

# defined function for object method3

    def diff_color(self,color):
        self.color = color

# defined function for object method4

    def diff_bodytype(self,bodytype):
        self.bodytype = bodytype

# defined function for object method5

    def pace(self,speed):
        self.speed = speed

vehicle = Car("lexus", "blue", "SUV", "fast")

vehicle.diff_model("Toyota")
vehicle.pace("fast!")
vehicle.my_func()