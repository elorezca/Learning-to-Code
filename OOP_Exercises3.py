class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def introduce(self):
        print(f"Hello my name is {self.first_name} {self.last_name}")
        

class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id
        
    def introduce(self):
        print(f"Hello my name is {self.first_name} {self.last_name}, and my employee ID is {self.employee_id}")
    
    
person = Person ("John","Doe")
person.introduce()
employee = Employee ("John","Doe", 153765)
employee.introduce()


class Shape:
    def __init__(self, color):
        self.color = color
        
    def description(self):
        print(f"The shape is {self.color}")

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
        
    def description(self):
        print(f"This square is {self.color} and has a side length of {self.side_length}")
        
shape = Shape ("blue")
square = Square ("red", 15)

shape.description()
square.description()


class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
    def drive(self):
        print(f"The vehicle is driving.")
            
            
class Car(Vehicle):
    def __init__(self):
        super().__init__(4)
    def drive(self, speed=None):
          if speed:
              print(f"The car is driving at {speed} mph")
          else:
              print("The car is driving")
          
vehicle = Vehicle(2)
vehicle.drive()

car = Car()
car.drive()
car.drive(60)



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
        
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        
    def perimeter(self):
        return self.width * 4

rectangle = Rectangle(4,5)
print(f"Rectangle Area: {rectangle.area()}")

square = Square(4)
print(f"Square area: {square.area()}")
print(f"Square Perimeter: {square.perimeter()}")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            