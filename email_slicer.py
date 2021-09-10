email = input("What is you email?\n").strip()

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

out = "Hello, you username is {} and the domain is {}"
print(out.format(username, domain))