# Lists

things = [ "Ewerton", "Willams", 14, 10, 1999, True, [2,3,7]]
print("things: ", things)
print("\"Silva\" in things ", "Silva" in things)
print("del things[-1]")
del things[-1]

print(things)

list_of_lists = [["a", "b", "c"], [10, 25, 48], [True, True, False]]
print(list_of_lists)
print("list_of_lists[0][2]: ", list_of_lists[0][2])

# adding items to list
things.append("Beth") # => this returns a NoneType. DO NOT reasign it
things.insert(0, "Beth")
things[0] = "Elisabeth";

# Adding lists
things = things + [2019]
print("things = things + [2019] -> ", things)
things = things + list("ABC")
print("things = things + list(\"ABC\") -> ", things)



# Tuples
# Tuples are imutable

my_tuple = 10,20
print("\n\nmy_tuple: ", my_tuple)

my_other_tuple = "word",10
print("my_other_tuple: ", my_other_tuple)

another_tuple = (True, "I'm nice")
print("another_tuple: ", another_tuple)

tuple_item1 = my_tuple.__getitem__(0)
tuple_item2 = my_tuple.__getitem__(1)

print("my_tuple.__getitem__(1): ", tuple_item1)
print("my_tuple.__getitem__(2): ", tuple_item2)

big_tuple = (1,3,5,7,9,12,34,456,567,345,456,7)
tup_elem = big_tuple[2] # returns 5

# we can convert a list to a tuple
list_1 = [1,2,3]
another_tup = tuple(list_1);

# multiple assignment
(a, b, c) = 12, 15, 35

# dictionary
my_dict = { "Name" : "Ewerton", "Age": 33}
print(my_dict)

print("my_dict[\"Name\"]: ", my_dict["Name"])

my_dict["Gender"] = "Masculine"
print(my_dict)

my_dict.pop("Gender") # or del my_dict["Gender"]
print(my_dict)

# getting the keys and values
keys = my_dict.keys()
vals = my_dict.values()

print(keys)
print(vals)

# indexing is not supported, so to get a specific item from the keys or values, 
# we need to first convert it to a list:

key0 = list(keys)[0]
val0 = list(vals)[0]

print(key0)
print(val0)

# getting all the items:
print(my_dict.items())