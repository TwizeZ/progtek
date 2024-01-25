
import copy
import math
import random

# Uppgift 1 (givet)

def scope_testing_function(x, x_list):
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x = 1
    x_list[0] = 1
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x_list = [1, 2, 3, 4]
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    return x

x_list = [11, 22, 33, 44]
x = 11
y = 22
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

scope_testing_function(x, x_list)
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2 (att skrivas)

def my_function(x):
    return (math.sin(x)**2 + x**2)

# Uppgift 3 (att skrivas)

def roll_dice(n):
    num = 0    # Variabel för att lagra summan av alla tärningskast.
    for i in range(0, n):
        num += random.randint(1, 6)
    return num

# Uppgift 4 (att skrivas)

def my_sort_list(num_list):
    list_sorted = False
    while list_sorted == False:
        list_sorted = True  # Om listan är sorterad kommer list_sorted att förbli True och while-loopen avslutas.
        for i in range(0, len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                list_sorted = False
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
    return num_list
                

# Uppgift 5 (att skrivas)

def bandit_language(sentence):
    vowels = "aeiouyåäö 1234567890"   # Alla vokaler och mellanslag i en sträng som sentence jämförs med.
    new_sentence = ""   # Tom sträng för att lagra den nya meningen.
    for letter in sentence:
        if letter in vowels:
            new_sentence += letter
        else:
            new_sentence += letter + "o" + letter
    return new_sentence
