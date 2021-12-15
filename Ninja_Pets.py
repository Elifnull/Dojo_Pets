import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        #self parameters
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        
        #methods
    def walk(self):
        self.pet.play()
        return self
    def bathe(self):
        self.pet.noise()
        return self
    def feed(self):
        self.pet.eat()

class Ronin(Ninja):
    def __init__(self, first_name, last_name, pet, treats, pet_food, owner_trick):
        super().__init__(first_name, last_name, pet, treats, pet_food)
        self.owner_trick = owner_trick
    
    def trick(self):
        print("yipppi Kiyayay")


sharko_tricks =("coo for affection", "deep sea dive")

sharko = Pet("sharko", "pigeon", sharko_tricks, 100, 120)



Mikial = Ninja( "Mike", "luvo", sharko, "food", "foodi")

Mikial.feed()