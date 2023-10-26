
phone_book = {
"Alice": "555-1234",
"Bob": "555-5678",
"Charlie": "555-2468"

}

name = input("Please enter either Alice, Bob, or Charlie. ")

print(f"The number of {name} is {phone_book[name]}")