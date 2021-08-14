import random

random_number = random.randint(0,10)

# to print random numbers
print(random_number)
rand  = random.random()
# print(rand)

lst = ["Samsung","i Phone","Nokia","Micromax"]
choice = random.choice(lst)
if (choice == "Micromax" or choice == "Samsung"):
        print("New version available for ")
print(choice)


