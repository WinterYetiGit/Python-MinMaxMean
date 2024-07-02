################################ 
# WinterYeti
# Date: 02/25/2024
# Python-MinMaxMean.py
# Version 1.0
# Description - A simply stats program for crunching the min, max and mean of a variable
# set of numbers provided by the user. Version 1.0 is designed for a singular execution.
# will expand in the future with a looping feature probably until user exits.
################################

import statistics

# Get input from user
num_values = int(input("Enter how many numbers you want to calculate the total of: "))
# Variables
numbers = []

# Loop for number input and output
for i in range(1, num_values + 1):
    num = float(input(f"Enter the {i}{'st' if i == 1 else 'th'} number: "))
    numbers.append(num)
    print(num, end=' ')
print()  

# Output in vertical format
print("All numbers vertically:")
for num in numbers:
    print(num)

# Calculations for total, max, min, and average
    
total = sum(numbers)        #new variables
max_num = max(numbers)
min_num = min(numbers)
average = statistics.mean(numbers)

# Output to user for calculations
print("\nResults:")
print("Total value for your input:", total)
print("The largest number (max):", max_num)
print("The smallest number (min):", min_num)
print("The average value for input:", average)
print("End of program. Thanks for trying it.")
1
# End program