item_count = {}  # Initialize an empty dictionary to store item counts

while True:
    item = input("Enter an item (or type 'done' to finish): ")
    
    if item.lower() == 'done':
        break
    
    # Increment the count for the entered item
    item_count[item] = item_count.get(item, 0) + 1

# Display the count of each item
print("Item counts:")
for item, count in item_count.items():
    print(f"{item}: {count}")