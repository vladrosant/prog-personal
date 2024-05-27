import random

names_string = input("type everone's name: ")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_payer = names[random_choice]

print(person_payer + " is going to buy the meal today")