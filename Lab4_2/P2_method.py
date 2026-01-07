#P2 Lab 4-2
from datetime import datetime

class Cat:
    # Class attributes
    species = "Felis catus"
    average_lifespan = 15
    total_cats = 0

    def __init__(self, name, age, breed, color):
        # Basic info
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

        # State tracking
        self.hungry = False
        self.energy = 100
        self.happiness = 100

        # Increment total cats
        Cat.total_cats += 1

    # Instance methods
    def meow(self):
        if self.hungry:
            return f"{self.name} meows loudly!! Feed me!"
        elif self.energy < 30:
            return f"{self.name} meows weakly :-/ I'm tired..."
        elif self.happiness < 50:
            return f"{self.name} meows sadly :-( Pet meee.."
        else:
            return f"{self.name} meows happily :-) Meaw~ =^.^="

    def eat(self, food_amount):
        if food_amount > 0:
            self.hungry = False
            self.energy = min(100, self.energy + food_amount // 2)
            self.happiness = min(100, self.happiness + food_amount // 3)
            return f"{self.name} eats {food_amount}g of food. \nEnergy = {self.energy}, Happiness = {self.happiness}"
        else:
            return f"{self.name} not in the mood to eat."

    def play(self, play_time):
        self.energy = max(0, self.energy - play_time * 5)
        self.happiness = min(100, self.happiness + play_time * 10)
        self.hungry = True
        return f"{self.name} played for {play_time} hours.\nEnergy = {self.energy}, Happiness = {self.happiness}"

    def sleep(self, hours):
        self.energy = min(100, self.energy + hours * 10)
        self.hungry = True
        return f"{self.name} slept for {hours} hours. \nEnergy = {self.energy}"

    def get_status(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Breed": self.breed,
            "Color": self.color,
            "Hungry": self.hungry,
            "Energy": self.energy,
            "Happiness": self.happiness
        }

    # Class methods
    @classmethod
    def from_birth_year(cls, name, breed, birth_y, color):
        current_y = datetime.now().year
        age = current_y - birth_y
        return cls(name, age, breed, color)

    @classmethod
    def get_species_info(cls):
        return f"Species: {cls.species}, Average Lifespan: {cls.average_lifespan} years"

    # Static methods
    @staticmethod
    def is_senior(age):
        return age > 7

    @staticmethod
    def calculate_healthy_food_amount(weight_kg):
        return f'For Dry food {weight_kg * 20} g./day For Wet food {weight_kg * 55} g./day'