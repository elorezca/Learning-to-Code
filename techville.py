
def move_forward():
        print("moving forward")

def turn(direction):
        print(f"turning {direction}")

def start_engine():
      print("starting engine")  

def stop_engine():
       print("stopping engine")

def round_about():
      print("You entered the roundabout")

hospital = "take the 1st exit"
mall = "take the 2nd exit"
airport = "take the 3rd exit"
univeristy = "take the 4th exit"
stadium = "take the 4th exit"



destination = input("Where do you want to go? ")

start_engine()
move_forward()

if destination == "library":
    turn('left')
    print("You arrived at the Library")
if destination == "tech park":
    turn('right')
    print("You have arrived at the tech park")
if destination == "hospital":
    round_about()
    print(hospital)
    print(f"You arrived at the hospital.")
if destination == "mall":
    round_about()
    print(mall)
    move_forward()
    turn("right")
    print("You arrived at the mall")
if destination == "airport":
    round_about()
    print(airport)
    print("You arrived at the airport")
if destination == "university" or destination == "stadium":
    round_about()
    print("You took exit 4")
    if destination == "university":
         turn("left")
         print("You arrived at the university")
    else:
         turn("right")
         print("You arrived at the airport")
else:
     print("invalid destination")