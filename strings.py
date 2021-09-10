hello = "Hello" + " World! "
print(hello)

print(hello * 3)

print("="*50)

a = "part "
b = 1
print(a + str(b))

# Format
book = "Jonh"
chapter = 3
verse = 16
string_formated = "{} {}:{}".format(book, chapter, verse)
print(string_formated)

#multiline string
multiline = """
lorem ipsum dolor sit amet 
and the rest I don't know
=)"""

anothermultiline = '''
We can write
a paragraph
here'''

print(multiline)
print(anothermultiline)