#Cool string methods

#count chars/word in a string
count_l = "hello".count("l")
print(count_l)
text = "happy birthday!"
print(text.count("day"))

#capitalization
name = "Hello World!"
print(name.lower())

name = "ewerton"
full_name = "ewerton willams"
print("name.upper() -", name.upper())
print("name.capitalize() -", name.capitalize())
print("full_name.title() - ", full_name.title())

# checks if the string is in upper case
print("name.isupper() - ", name.isupper())

#chekc if the string contains just letters
print("name.isalpha() - ", name.isalpha())

x = "1234"
print("x = '1234'")
print("x.isalnum() - ", x.isalnum())
print("x.isdigit() - ", x.isdigit())

wife = "My wife is a very nice person"
print(wife.__contains__("nice"))
print(wife.find("is"))

try:
#will throw an error
    print(wife.index("!"))
except ValueError as error:
    print(error)

#with find it will return -1
print(wife.find("!"))

crazy_str = "00000000000000happybirthday00000000"
print(crazy_str.strip("0"))
print(crazy_str.rstrip("0"))
print(crazy_str.lstrip("0"))

name = " Ewerton"
print(name.strip())

name = input("What is your name? ").strip()
print(name)

print("length: ", len(name))

#doc here: https://docs.python.org/3/library/stdtypes.html#string-methods