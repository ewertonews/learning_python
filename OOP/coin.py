import random

class Coin:
    def __init__(self, is_rare=False, is_clean=True, **kwargs):
        self.is_rare = is_rare
        self.is_clean = is_clean

        for key,value in kwargs.items():
            #self.key = value
            setattr(self,key,value)

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        
        if self.is_clean:
            self.colour= self.clean_colour
        else:
            self.colour = self.rusty_colour

    #destructor
    def __del__(self):
        print("Coin Spent!")

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    # overriding str() method
    def __str__(self):
        if self.original_value >= 1:
            return "${} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))

#inheritance - instead of self, receives the parent / base class
class Pound(Coin):
    def __init__(self):
        data = {
            "original_value":1.00,
            "clean_colour":"gold",
            "rusty_colour":"greenish",
            "num_edges":1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }

        super().__init__(**data)


class One_pence(Coin):
    def __init__(self):
        data = {
            "original_value":0.01,
            "clean_colour":"bronze",
            "rusty_colour":"brownish",
            "num_edges":1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
        }

        super().__init__(**data)

class Two_pence(Coin):
    def __init__(self):
        data = {
            "original_value":0.02,
            "clean_colour":"bronze",
            "rusty_colour":"brownish",
            "num_edges":1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
        }

        super().__init__(**data)

class Five_pence(Coin):
    def __init__(self):
        data = {
            "original_value":0.05,
            "clean_colour":"silver",
            "rusty_colour": None,
            "num_edges":1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
        }

        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


coins = [One_pence(), Two_pence(), Five_pence(), Pound()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.mass]
    string = "{} - Colour: {}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
    print(string)
