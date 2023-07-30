'''
Title: Fermat's Last Theorem Near Miss Finder
File: fermat_last_theorem_miss_finder.py
No external files necessary to run the program
No external files created by the program
Programmer: Andrew J. Milligan
Email: andrewjmilligan@lewisu.edu
Course: Software Engineering, CPSC 60500
Date: July 30, 2023
This program helps an interactive user search for “near misses” of the form (x, y, z, n, k) in the formula xn + yn = zn.
Resources: Numberfile on Youtube, www.geeksforgeeks.org, www.w3schools.com
'''

# The built-in sys module provides access to some variables used or maintained
# by the Python interpreter and to functions that interact strongly with the interpreter.
import sys

def main():
    # User input for n and k that ensures valid user inputs for the necessary range
    n = 0
    while not 2 < n < 12:
        try:
            n = float(input("Enter the value for n (2<n<12): "))
        except ValueError:
            print("Invalid input, please enter a valid number for n.")
            continue

    k = 0
    while k <= 10:
        try:
            k = float(input("Enter the value for k (k>10): "))
        except ValueError:
            print("Invalid input, please enter a valid number for k.")
            continue

    # Initialize minimum relative miss and absolute miss
    # Start with infinity because any real number will be smaller than infinity
    min_relative_miss = float('inf')
    min_absolute_miss = float('inf')

    # Variables to hold the coordinates (x, y, z) that correspond to the smallest misses
    x_min_miss, y_min_miss, z_min_miss = None, None, None

    # Counter for near misses
    near_misses = 0

    total_iterations = (int(k) - 10 + 1) ** 2
    iteration_counter = 0
    next_checkpoint = total_iterations / 10  # The point at which we print the first progress update

    # Iterating over possible x and y values
    for x in range(10, int(k) + 1):
        for y in range(10, int(k) + 1):

            # Update the iteration counter and check if it's time for a progress update
            iteration_counter += 1
            if iteration_counter >= next_checkpoint:
                print(f"Completed {100 * iteration_counter / total_iterations:.1f}% of calculations, "
                      f"found {near_misses} near misses so far.")
                next_checkpoint += total_iterations / 10

            # Calculate xn + yn
            try:
                sum_xn_yn = pow(x, n) + pow(y, n)
            except OverflowError:
                print(f"Calculation overflow for x={x}, y={y}. Skipping this pair.")
                continue

            # Find potential z values that bracket sum_xn_yn
            try:
                z = pow(sum_xn_yn, 1 / n)  # z might not be an integer
            except OverflowError:
                print(f"Calculation overflow for x={x}, y={y}. Skipping this pair.")
                continue

            z_floor = int(z)
            z_ceil = z_floor + 1  # z_ceil = z_floor + 1, to bracket sum_xn_yn

            # Calculate misses
            try:
                miss1 = abs(sum_xn_yn - pow(z_floor, n))
                miss2 = abs(sum_xn_yn - pow(z_ceil, n))
            except OverflowError:
                print(f"Calculation overflow for x={x}, y={y}, z={z}. Skipping this pair.")
                continue

            # Find which z value (z_floor or z_ceil) provides a closer match
            if miss1 < miss2:
                miss = miss1
                z_closest = z_floor
            else:
                miss = miss2
                z_closest = z_ceil

            # Calculate the relative size of the miss
            relative_miss = miss / sum_xn_yn

            # Check if this is the smallest absolute and relative miss so far
            if miss < min_absolute_miss:
                min_absolute_miss = miss
                min_relative_miss = relative_miss
                x_min_miss, y_min_miss, z_min_miss = x, y, z_closest
                near_misses += 1

                # Check if the relative miss can be printed without memory errors
                if len(str(relative_miss)) <= 27:  # Decimal plus 25 digits plus point
                    print(f"x={x}, y={y}, z={z_closest}, miss={miss}, relative miss={relative_miss}")
                else:
                    print(f"x={x}, y={y}, z={z_closest}, miss={miss}, relative miss is too large to print.")

    # Print the total number of near misses found and the smallest miss
    print(f"\nTotal number of near misses found: {near_misses}")
    print(f"The smallest miss is {min_absolute_miss} at x={x_min_miss}, y={y_min_miss}, z={z_min_miss} with relative miss={min_relative_miss}")

# End of program

while True:
    main()
    continue_program = input("Would you like to run the program again? Enter Y for yes and N for no: ")
    if continue_program.lower() != "y":
        break
