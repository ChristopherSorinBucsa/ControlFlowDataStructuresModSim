"""
Name: Christopher Bucsa
"""
import math 
"""
Problem 1
"""
print("\n",40*"-","\n","Problem 1:\n",40*"-")

# 1a
print("1a.)\nFirst 10 odd numbers:")
for e in range(1,20,2):
        print(e, end=", ")

print("\n")

#1b
print("1b.)\nFirst 10 even numbers, in reverse:")
for e in range(20,1,-2):
    print(e, end=", ")

print("\n")

#1c
print("1c.)\nFirst 10 non-zero multiples of 13:")
i = 1
while i <11:
    print(13 * i,end=", ")
    i = i + 1

print("\n")

#1d
print("1d.)")
sum_digits = 0
user_num = str(input("Enter number: ")) # Since int's are non-iterable, need to convert to String for python

for e in user_num: # For every element in this String - "123", "5", "980"  
    digit = int(e) # Cast each element to an int "1" becomes 1, etc. 
    sum_digits = sum_digits + digit # Add these int-casted elements in x to the total sum

print("Sum of digits in your number is: ", sum_digits, end=", ")
print("\n")

#1e
print("1e.)")
product_digits = 1 # Create base for product, can't be zero or result will always be 0
user_num2 = str(input("Enter another number: ")) # Need to convert user number to string again in order to iterate

for e in user_num2: # For each element in string
    digit2 = int(e) # Need to cast to int to multiply digits
    product_digits = product_digits * digit2 # Multiply digits together and update

print("Product of digits in your number is: ", product_digits, end=", ")
print("\n")

#1f
print("1f.)\nAll numbers between 100 and 500 divisible by 11, but not by 2:")
# between 100 and 500, can use "in rage()" function
for e in range(100,501):
    if e%11 == 0 and e%2 != 0: # Divisible by 11? AND Not divisible by 2?  If True, print
        print(e, end=", ") 

print("\n")
    
"""
Problem 2
"""
print("\n",40*"-","\n","Problem 2:\n",40*"-")

import random  
random.seed(123) # initialize random number generator algorithm, if inside for loop, same number will be printed
rand_list = [] # Create empty list to store values, will populate in loop

for e in range(1,1001): # Need 1000 elements in list
    rand_int = random.randint(1,10)  # Create random integer, could also use ".randint()" method in "append" method but too lengthy
    rand_list.append(rand_int)  # Adds random integer to list, for each element "e" 1000 total
    

# Print first 10 number's in list "rand_list", need 0-9 index
print("First 10 elements in list: ", rand_list[ : 10], "\n")
print("Total number of elements in list: ", len(rand_list), "\n") # Added for simplicity

# Convert list to tuple, called "rand_tuple" 
rand_tuple = (rand_list)
# Print the length of new tuple, should be the same as list - 1000
print("After conversion, number of elements in tuple: ", len(rand_tuple), "\n") 

# Can also store the list itself as an element of the tuple, resulting in a 
# tuple that contains one element - the list, "rand_list" -- rand_tuple = ([rand_list]) 

# Count number of odd numbers in new tuple
# Need counter variable
odd_count = 0 # Initialize to 0 
for e in rand_tuple:
    if e%2 != 0: # if remainder of element "e" / 2 is not 0, number is odd
       odd_count = odd_count + 1 # So add to total count of odds

print("Total number of odd elements in tuple: ", odd_count, "\n")

"""
Problem 3
"""
print("\n",40*"-","\n","Problem 3:\n",40*"-")

# Need to check numbers from 1 to 1000 for perfect
# Use nested loop to go from 1-1000 and inner loop to cycle
# through each numbers range (2=1/3=1,2/4=1,2,3/etc) don't
# want to check if number is divisible by zero though so
# need to start inner loop's range at 1 not 0

for e in range(1,1001):
    divisor_sum = 0 # Will use to sum a numbers divisors, needs to reset after each iteration
    for e2 in range(1,e):
        if e%e2 == 0: #Look for divisors
            divisor_sum = divisor_sum + e2 # If divisor, add to total sum
    if divisor_sum == e: # Aligned with inner loop to make sure all numbers in range of "e" are checked
        print("Perfect Number: ", e) # If sum of divisors is equal to the number itself, we can output it to screen
        
"""
Problem 4
"""
print("\n",40*"-","\n","Problem 4:\n",40*"-")
#4a
gravity_acceleration = (-9.81)**2 # When falling, travels at 9.81 meters per second
beginning_speed = 15 # Shoots out at 15 meters per second
beginning_height = 0 # Initial height of projectile
launch_angle = (math.pi)/3 # 60 Degrees converted to radians, as needed by trig functions(cos,sin,tan, etc.)

# 4b
print("4b/4c.)")
trajectory_values = [] # Empty list to store trajectory values for projectile

for x in range(0,11):
    trajectory_values.append(x * (math.tan(launch_angle)) + ((gravity_acceleration * (x**2)) / (2 * (beginning_speed**2) * (math.cos(launch_angle)**2))) + (beginning_height))
    print(f"x{x} = {trajectory_values[x]:.2f} m/s")