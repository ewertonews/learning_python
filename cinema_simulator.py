films = {
    "Finding Dory": [3,5], # age allowed, number of tickts
    "Bourne" : [18,5],
    "Tarzan": [15,1],
    "Ghost Busters":[12,5]
}

while True:
    choice = input("What film would you like to watch?\n").strip().title()
    
    if choice in films:
        #pass - do nothing.. just go on 🤷‍♂️
        if films[choice][1] > 0:
            films[choice][1] = films[choice][1] - 1
        else:
            print("Sorry.. no more tickets left for this film.")
            continue

        age = int(input("How old are you?\n").strip())

        if age >= films[choice][0]:            
            print("Enjoy the film!")
        else:
            print("You are too young to watch to see that filme 😟")
    else:
        print("We don't have that film...")