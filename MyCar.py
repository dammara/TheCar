# Markhus Dammar
# 11/11/19
# This is the exe for car

from Car import Car

mycar = Car("Pontiac", "G6", "Gray", "2008", 1200, "1650")


print(f"The car was made by {mycar.make}")
print(f"""
The model of the {mycar.make} is {mycar.model}.
The {mycar.make} {mycar.model} is {mycar.color}.
The {mycar.make} {mycar.model} was manufactured in {mycar.year}.
The {mycar.make} {mycar.model} has {mycar.mileage} miles on it.
The {mycar.make} {mycar.model} costed ${mycar.price}.
""")
input("Press Enter to Continue")

choice = input("\nWanna go for a drive? >>>")

if choice == "y" or choice =="Y" or choice == "yes" or choice == "Yes":
    mycar.mileage = mycar.mileage + 10
    print(f"The {mycar.make} {mycar.model}'s odometer is now at {mycar.mileage}")
else:
    print("Okay, not a problem")

choice_color = input("What color would you rather have the car? >>>")
print(f"The {mycar.make} {mycar.model} is now {choice_color}")



