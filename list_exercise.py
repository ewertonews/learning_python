def remove_user(known_users, name):
    remove = input("Would you like to be removed from the system? (y/n)\n").lower()
    if remove == "y":
        known_users.remove(name)

def ask_if_user_wants_to_be_added(known_users, name):
    print("Hmmn.. I don't think I have met you yet {}".format(name))
    add_me = input("Would you like to be added to the system? (y/n)").strip().lower()

    if add_me == "y":
        known_users.append(name.capitalize())


known_users = ["Ewerton", "Beth", "Remilton", "Maisa", "Israel", "Paloma"]
print(len(known_users))

name = ""

while name != "Quit":
    print("Hi, my name is Travis")
    name = input("What is your name?\n").strip().capitalize()

    if name in known_users:
        print("Hello {}, your entrance is allowed. Welcome.".format(name))
        remove_user(known_users, name)

    else:
        ask_if_user_wants_to_be_added(known_users, name)