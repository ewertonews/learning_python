name = input("What is your name?\n")
age = input("How old are you?\n")
live_in = input("Where do you live?\n")

string = "Hello {}! Good to know you are {} years old and live in {}"
print(string.format(name, age, live_in))