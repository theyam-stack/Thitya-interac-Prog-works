from P2_method import Cat

meow1 = Cat("Salit", 7, "Thai Ban", "Patched Tabby")
meow2 = Cat("Moomin", 8, "Thai Ban", "White mixed orange")
meow3 = Cat.from_birth_year("Tiger", "Domestic Shorthair", 2021, "Orange Tabby")

print(" # Class Info")
print(f"Total cats created: {Cat.total_cats}")
print(Cat.get_species_info())

print("\n # First Cat")
print(meow1.meow())
print(meow1.play(8))
print(meow1.eat(50))
print(meow1.sleep(3))
print(meow1.get_status())

print("\n # Second Cat")
meow2.energy = 29 
print(meow2.meow())
print(meow2.eat(0))
print(meow2.sleep(12))
print(meow2.get_status())

print("\n # Third Cat")
meow3.happiness = 40 
print(meow3.meow())
print(meow3.play(0))
print(meow3.get_status())

print("\n # Static Methods")
print(f"Is {meow3.name} senior? {Cat.is_senior(meow3.age)}")
print(f"Is {meow1.name} senior? {Cat.is_senior(meow1.age)}")
print(f"Is {meow2.name} senior? {Cat.is_senior(meow2.age)}")
print(f"Recommended food for {meow2.name} (4kg): {Cat.calculate_healthy_food_amount(4)}")