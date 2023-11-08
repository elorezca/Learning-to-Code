
water_level = 5

while water_level > 0:
    print(f"Watering plant. Waterlevel: {water_level}")
    water_level -= 1
if water_level == 0:
    print("The watering can is now empty.")