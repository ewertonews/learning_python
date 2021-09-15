# get all even numbers from 1 to 100:
even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)

print("\r")

# get all odd numbers to the power of 2 from 1 to 100:
crazy_numbers = [y**2 for y in range(1,101) if y % 2 != 0]
print(crazy_numbers)

print("\r")

# combines the elements of two lists if they are not equal:
combination_tuples = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combination_tuples)
#more here: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions