# Importen kör my_module.py en gång.
import my_module
from my_module import *


# Uppgift 1 (givet)

# Här ändras värdet på x och y, och scope_testing_function körs från my_moduble.py.
y = 222
x = 111
x_list = [111, 222, 333, 444]
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
my_module.scope_testing_function(x, x_list)
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2 (att skrivas)

print(my_function(1))    # Resultatet blir 1.708073418273571.

# Uppgift 3 (att skrivas)

print(roll_dice(3))

# Uppgift 4 (att skrivas)

example_list = [10, 4, 7, 2, 21, 9, 5, 3, 1, 8, 6]
print(my_sort_list(example_list))


# Uppgift 5 (att skrivas)

sentence = "jag talar rövarspråket"
print(bandit_language(sentence)) # Resultat: "jojagog totalolaror rorövovarorsospoproråkoketot"

# Uppgift 6 (givet)

animals = {'tiger': ['claws', 'sharp teeth', 'four legs', 'stripes'],
           'elephant': ['trunk', 'four legs', 'big ears', 'gray skin'],
           'human': ['two legs', 'funny looking ears', 'a sense of humor']
           }

# Uppgift 6 (att skrivas)

def make_bandit_dictionary(dictionary):
    bandit_dict = {}    # Tomt dictionary för att lagra nytt dictionary.
    for key in dictionary:
        temp_list = []   # Tom lista för att lagra ny lista för varje key.
        for item in dictionary[key]:  # Loopar igenom varje item i listan som key pekar på.
            temp_list.append(bandit_language(item))
        bandit_dict[key] = temp_list
    return bandit_dict

print(make_bandit_dictionary(animals))