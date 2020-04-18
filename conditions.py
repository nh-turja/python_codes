weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")


if unit.upper()=="L":
    print("You are " + str(0.45 * int(weight))+ " kilos.")
elif unit.upper()=="K":
    print("You are " + str(2.2 * int(weight))+ " kilos.")
else:
    print("Sorry, cannot be converted.")