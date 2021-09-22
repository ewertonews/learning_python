a = 250

def f1():
    global a #states that this function will use/modify the global variable "a"
    a = 100
    print(a)

def f2():
     a = 50 #local
     print(a)

print(a)

# output:
# 100
# 50
# 100

# Default Parameter

def about(name, age, likes = "Python"):
    sentence = "Meet {}! They are {} years ond they  like {}".format(name, age, likes)
    return sentence

# Packing and Unpacking using *args and **kwargs
print(1, 2, 3, 4, 5) #it will work!
# result will be 1 2 3 4 5

# printing a list 
numbers = [1,2,3,4,5];
print(numbers)
# result will be [1,2,3,4,5]

# unpacking the list
print(*numbers)
# result will be 1 2 3 4 5
# We can unpack any iterable data type before they go into functions

print(*"abc")

def sum(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

result = sum(1,2,3,4,5,6,7,8,9)
print(result)

# Packing arguments
dictionary = {"name": "Ewerton", "age": 33, "likes": "Python and C#"}

   
# using function defined in line 21
print(about(**dictionary))

def foo(**kwarks): # convesion for key work arguments 
    for key,value in kwarks.items():
        print("{}:{}".format(key, value))

foo(Beth = "Female", Ewerton = "Male", Jane= "female")