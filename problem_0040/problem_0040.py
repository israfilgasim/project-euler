numbers = ''# String to store the numbers
counter = 1 # Counter to keep track of the number of digits

while len(numbers) < 1000000: # Loop until the string is 1 million digits long
    numbers += str(counter) # Add the number to the string
    counter += 1 # Increment the counter

sum = int(numbers[0]) * int(numbers[9]) * int(numbers[99]) * int(numbers[999]) * int(numbers[9999]) * int(numbers[99999]) * int(numbers[999999]) 
# Multiply the digits together

print(sum) # Print the sum

#ans: 210