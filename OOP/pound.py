import random

class Pound:
    #constructor
    def __init__(self, is_rare=False):
        self.is_rare = is_rare

        if self.is_rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True        

    #destructor
    def __del__(self):
        print("Coin Spent!")

    # every class method must receive self (or whatever it was used in line 6 - could be 'this')
    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

coin1 = Pound()

print(coin1.colour)
print(coin1.value)

coin1.value = 5.0
del coin1 

print(coin1.value)
