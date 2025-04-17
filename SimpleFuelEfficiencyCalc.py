# William Starks
# 2/24/2025
# CSCI - 1170
# Did not use AI
# This program converts fuel efficiency from kilometers per liter
# to miles per gallon (mpg) and determines if the car meets the target efficiency.

# Needed Constants
CONVERSION_FACTOR = 2.352 
TARGET_EFFICIENCY = 50 
WAIVER_THRESHOLD = 0.95  

# Get user input for fuel efficiency in kpl
kpl = float(input("Enter the fuel efficiency in kilometers per liter: "))

# Convert kpl to mpg
mpg = kpl * CONVERSION_FACTOR

# Display mpg
print(f"Fuel efficiency: {mpg:.2f} miles per gallon.")

# Determine if the car meets the target efficiency
if mpg >= TARGET_EFFICIENCY:
    print("This car meets or exceeds the target fuel efficiency.")
elif mpg >= TARGET_EFFICIENCY * WAIVER_THRESHOLD:
    print("This car does not meet the target fuel efficiency but may be eligible for a waiver.")
else:
    print("This car does not meet the target fuel efficiency and is not eligible for a waiver.")

# Final message
print("Thank you for using the fuel efficiency calculator.")
