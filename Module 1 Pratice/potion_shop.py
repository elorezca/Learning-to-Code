# Define the dictionary of potions and their ingredients
potions = {
    "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"],
    "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"],
    "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"]
}

# Display the list of available potions
print ("Welcome to the Magic Potion Shop!")
print("Here are the potions we offer:")
for potion in potions.keys():
    print(potion)

# Ask the user to choose a potion
selected_potion = input("Which potion would you like to buy ingredients for? ")

print("")

# Check if the selected potion exists in the dictionary
if selected_potion in potions:
    ingredients = potions[selected_potion]

    print(f"The ingredients for {selected_potion} are:")
    print(f"{ingredients[0]}")
    print(f"{ingredients[1]}")
    print(f"{ingredients[2]}")
    
    print("")

    print("Let's start buying the ingredients!")

    # Initialize a list to track purchased ingredients
    purchased_ingredients = []
    
    while ingredients:
        # Ask the user if they want to buy the next ingredient
        buy_next = input(f"Do you want to buy {ingredients[0]} (yes/no): ").lower()
        
        if buy_next == "yes":
            ingredient = ingredients.pop(0)
            purchased_ingredients.append(ingredient)
            print(f"Successfully purchased {ingredient}.")
        else:
            print("You chose to stop shopping.")
            break

    # Check if all ingredients are purchased
    if not ingredients:
        print(f"Congratulations! You bought all the ingredients for {selected_potion}.")
else:
    print("Invalid potion choice. Please choose a potion from the list.")
