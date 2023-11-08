
# fruits = ["cherry", "banana", "apple", "date"]

# print(fruits)

# new_fruit = input("Please enter a name of a fruit to add to the list ")

# fruits.append(new_fruit)

# print(fruits)

# fruits.pop(1)

# print(fruits)

# fruits.sort()

# print(fruits)

# student = {"name": "John Doe", "age":

# print(student)

# student["Major"] = "Electiral Engineering"

# print(student)

# student["year"] = "Senior"

# print(student)


# books = [
#     {"title": "Harry Potter", "author": "J.K. Rowling", "year": 1994},
#     {"title": "Animorphs", "author": "K.A Applegate", "year": 1996},
#     {"title": "Demonata", "author": "Darren Shawn", "year": 2000}
# ]

# print("Title of the second book:", books[1]["title"])

# print("Year the thrid book was published in:", books[2]["year"])

# for book in books:
#     print("Title:", book["title"])
#     print("Author:", book["author"])
#     print("Year:", book["year"])


courses = {
    "math": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "history": ["Frank", "Grace", "Hannah", "Ivy", "Jack"],
    "chemistry": ["Kate", "Liam", "Mia", "Noah", "Olivia"],
}

print("Students taking Math:", courses["math"])

courses["math"].extend(["james", "bobby", "aaron", "michelle", "allison"])

print("5 Students joined Math:", courses["math"])

courses["history"].pop(2)

print("History:", courses["history"])

print("Students in chemistry:", courses["chemistry"])

courses["physics"]=["Al", "rick", "mary", "arnold"]

print("Physics:", courses["physics"])

