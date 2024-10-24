weight = float(input("How many pounds does your package weigh? "))
shipPref = None
groundRates = [1.50, 3.00, 4.00, 4.75] 
droneRates = [4.00, 9.00, 12.00, 14.25]

while shipPref not in [1, 2, 3]:
  try:
    shipPref = int(input("""
    Which shipping method would you prefer?

    1) Ground Shipping 
    2) Ground Shipping Premium
    3) Drone Shipping

    (Please input the corresponding number)
    """))
        
    if shipPref not in [1, 2, 3]:
      print("Sorry, that wasn't a valid option.")
  except ValueError:
    print("Please enter a number.")

print("Yay!")

total = 0.00

match shipPref:
  case 1:
    if weight <= 2:
      total = weight * groundRates[0]
    elif weight > 2 and weight <= 6:
      total = weight * groundRates[1]
    elif weight > 6 and weight <= 10:
      total = weight * groundRates[2]
    else:
      total = weight * groundRates[3]
    total += 20
  case 2:
    total = 125.00
  case 3:
    if weight <= 2:
      total = weight * droneRates[0]
    elif weight > 2 and weight <= 6:
        total = weight * droneRates[1]
    elif weight > 6 and weight <= 10:
        total = weight * droneRates[2]
    else:
        total = weight * droneRates[3]

print("And your total is: $" + str(total))

