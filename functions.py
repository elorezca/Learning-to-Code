
# dollarizer = input("Dollarizer: ")

# dollarizer1 = dollarizer.replace("s","$")

# print (f"Dollarizer:  {dollarizer1}")

# eurizer = input("Eurizer: ")

# eurizer1 = eurizer.replace("e","€")

# print (f"Eurizer: {eurizer1}")

# replacer = input("Replacer: ")

# dollarizer_eurizer = replacer.replace("s", "$").replace("e", "€")

# print (f"Replacer: {dollarizer_eurizer}")

# wonky = str.maketrans({"s": "$", "e": "€","l":"£"})

# input_string = input("Wonky Text: ")

# output_string = input_string.translate(wonky)

# print(output_string)

# celsiuis = int(input("Celsius to Fahrenheit: "))

# fahrenheit = (9/5 * celsiuis) + 32

# print ("Celsius to Fahrenheit:", fahrenheit)

# age = int(input("How old are you: "))

# age_in_days = age * 365

# print (f"Age In Days: {age_in_days}")

# output_string = str("Simple Intrest: ")

# p = float(input("Time in Princial Ammount: "))
# r = float(input("Time in Rate of Intrest: "))
# t = float(input("Time in Time in Years: "))
# d = float(input("Desired Amount: "))

# SI = p * r * t

# print (f"{output_string} {SI}")

# desired_amount = SI >= d

# print (f"Desired amount reached: {desired_amount}")

import math

# square_perimeter = int(input("Please enter the length of the square: "))

# P = 4 * square_perimeter

# print (f"The Perimiter of the Sqaure is: {P}")

# circle_details = float(input("Please enter the radius of a circle: "))

# radius = circle_details * 2
# circumference = 2 * math.pi * circle_details

# print (f"The Radius is: {radius}")
# print (f"The Circumference is: {circumference}")

square_length = float(input("Please enter the length of the square: "))

circle_radius = float(input("Please enter the radius of a circle: "))

perimiter_square = square_length * 4

area_square = square_length**2

circle_circumference = 2 * math.pi * circle_radius

circle_area = math.pi * circle_radius**2

if perimiter_square > circle_circumference:print("The Sqaure has a larger perimiter")

else:print ("The Circle has a larger circumference")

if area_square > circle_area:print("The Sqaure has a larger arear")

else:print ("The Circle has a larger area")


