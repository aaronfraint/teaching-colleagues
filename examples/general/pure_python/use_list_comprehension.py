# # List comprehension in Python
#
# You can simplify an `if` statement to a single line using Python's list comprehension abilities.

# Get a list of numbers
num_list = range(1, 50)

# +
# Use an if statement to make a list that only has even numbers
even_list = []
for num in num_list:
    if num % 2 == 0:
        even_list.append(num)
        
print(even_list)

# +
# Do the same thing with a single line of code
even_list = [num for num in num_list if num % 2 == 0]

print(even_list)
# -

# #### Depending on the quantity and complexity of your conditions, this could make your code easier or harder to read
#
# Use each approach as warranted.
