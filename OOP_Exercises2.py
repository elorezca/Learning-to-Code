
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return self.radius * 2
circle = Circle(5)

print(f"Diameter: {circle.diameter}")

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value:
            self._first_name = value
        else:
            raise ValueError("First name cannot be empty")

    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, value):
        if value:
            self._last_name = value
        else:
            raise ValueError("Last name cannot be empty")

person = Person("John", "Doe")
print(f"{person.first_name}, {person.last_name}")
person.first_name = "Jane"
person.last_name = "Smith"
print(f"{person.first_name}, {person.last_name}")


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive number")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive number")
    
    @property
    def area(self):
        return self.width * self.height
    
area_rec = Rectangle(15, 18)
print(f"The width of the rectangle is {area_rec.width} and the height is {area_rec.height} and the area is {area_rec.area}")

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self._balance = initial_balance
        
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        self._balance -= amount
        
    def is_overdrawn(self):
        return self._balance < 0            
    
    
account = BankAccount(154658, 1000)

print(f"Your starting balance was {account.balance}")

account.deposit(2000)

print(f"You deposited 2000 your new balance is {account.balance}")