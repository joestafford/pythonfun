import sys

# Prompting Customer for Rental Code and set input as string variable.
rentalCode = input('(B)udget, (D)aily, or (W)eekly rental?\n').upper()

# Initializing Variable "lengthRented".
lengthRented = 0

# Using If/Else branch logic to determine which prompt to display based on rentalCode.
if rentalCode == 'W':
    lengthRented = input('Number of Weeks Rented:\n')
else:
    lengthRented = input('Number of Days Rented:\n')

# Convert lengthRented to integer.
lengthRented = int(lengthRented)

# Set variables Rental Code charges.
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

# Using If/elif branch logic to determine appropriate rental period and rate to determine base charge.
if rentalCode == 'W':
    baseCharge = lengthRented * weekly_charge
elif rentalCode == 'B':
    baseCharge = lengthRented * budget_charge
elif rentalCode == 'D':
    baseCharge = lengthRented * daily_charge

# Prompting for Starting Odometer Reading & change variable to integer.
odoStart = input('Starting Odometer Reading:\n')
odoStart = int(odoStart)

# Prompting for Ending Odometer Reading & change variable to integer.
odoEnd = input('Ending Odometer Reading:\n')
odoEnd = int(odoEnd)

# Calculate total miles driven and save as variable.
totalMiles = odoEnd - odoStart

#  Initializing variables then using If/elif branch logic to determine which mileage charge formula to use based on rentalCode.
mileCharge = 0.00
basePerMileCharge = 0.25
weeklyMilesCharge = 100.00
weeklyMiles = 900
dailyMiles = 100

if rentalCode == 'W':
    averageWeekMiles = totalMiles / lengthRented
    if averageWeekMiles > weeklyMiles:
        mileCharge = weeklyMilesCharge * lengthRented

if rentalCode == 'D':
    averageDayMiles = totalMiles / lengthRented
    if averageDayMiles > dailyMiles:
        extraMiles = averageDayMiles - dailyMiles
        mileCharge = extraMiles * lengthRented * basePerMileCharge

if rentalCode == 'B':
    mileCharge = totalMiles * basePerMileCharge

# Calculate Total Amount Due and set as variable.
amtDue = baseCharge + mileCharge

# Display the results of the rental calculation.  Integers set as strings and "amtDue" formatted to decimal.
print('Rental Summary')

print('Rental Code: ' + rentalCode)

print('Rental Period: ' + str(lengthRented))

print('Starting Odometer: ' + str(odoStart))

print('Ending Odometer: ' + str(odoEnd))

print('Miles Driven: ' + str(totalMiles))

print('Amount Due: $%.2f' % amtDue)