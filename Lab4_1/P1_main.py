# Main program to test Cat class
from P1_Cat import Cat
from datetime import datetime, timedelta
# Add 3 cats 
cat1 = Cat("Salit", "Siamese", 2, "Pinpak wick")
cat2 = Cat("Moomin", "Thai Ban", 4, "Mary Potter")
cat3 = Cat("Tiger", "Domestic Shorthair", 3, "Viewwie")

print("\n # First Cat")
print(f"Last date in for {cat1.name}: {cat1.get_time_in()}")
cat1.greet()

print("\n # Second Cat")
print(f"Last date out for {cat2.name}: {cat2.get_time_out()}")
# Change date_out to be +2 days from now
date_out = datetime.now() + timedelta(days=2)
cat2.set_time_out(date_out)
print(f"New last date out for {cat2.name}: {cat2.get_time_out()}")

print("\n # Third Cat")
cat3.owner = "Tony"
cat3.age = 5
print(f"New owner for {cat3.name}: {cat3.owner}")
print(f"New age for {cat3.name}: {cat3.age}")

print("\n # Details of all 3 cats")
cat1.print_cat()
cat2.print_cat()
cat3.print_cat()

print(f"Current Total number of cats: {Cat.get_num()}")

Cat.reset_cat()
print(f"Total number of cats after reset: {Cat.get_num()}")