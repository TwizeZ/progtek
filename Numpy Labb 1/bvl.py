import numpy as np
import matplotlib.pyplot as plt
import scipy as sp



cost = np.array([1.95, 0.49, 0.99, 1.2, 31.96, 6.5, 6.95, 0.95, 0.49, 2.99, 2.69, 5.99, 1.09, 1.99, 2.99,
                     12.9, 6.9, 0.99, 17.9, 2.99, 6.99, 7.99, 19.9, 8.99, 7.99, 1000])
protein_list = [930, 2000, 1100, 13700, 40440, 36490, 14950, 260, 1280, 900, 2820, 2000, 0, 1090, 2900, 0, 3090, 3220,
                24900, 12600, 19900, 19190, 20000, 21500, 19400, 0]
carbohydrate_list = [9600, 17000, 9340, 72500, 41220, 30160, 16700, 13810, 5800, 3900, 6640, 8530, 97330, 22840, 3600,
                     0, 3260, 5260, 1300, 1120, 0, 0, 0, 0, 700, 0]
fat_list = [240, 90, 100, 1870, 7610, 19940, 60750, 170, 100, 200, 370, 14660, 0, 330, 400, 100000, 340, 3250, 33100,
            10600, 8670, 12440, 16000, 6900, 3800, 0]
vit_a_list = [0.835, 0.0006, 0, 0, 0, 0.001, 0.001, 0.003, 0, 0.042, 0.031, 0.007, 0, 0, 0.469, 0, 0, 0.046, 0.602,
              0.149, 0.009, 0.012, 0.026, 0.024, 9.5, 0]
vit_b1_list = [0.066, 0.08, 0.046, 0.447, 10.99, 0.874, 0.643, 0.017, 0.061, 0.037, 0.071, 0.067, 0.008, 0.031, 0.078,
               0, 0.081, 0.044, 0.03, 0.066, 0.79, 0.23, 0.12, 0.19, 0.48, 0]
vit_b2_list = [0.058, 0.03, 0.027, 0.215, 4, 0.87, 0.113, 0.026, 0.04, 0, 0.117, 0.13, 0.007, 0.073, 0.189, 0, 0.402,
               0.183, 0.32, 0.5, 0.28, 0.2, 0.11, 0.15, 2.4, 0]
vit_b3_list = [0.983, 1.05, 0.116, 6.365, 40.3, 1.623, 1.8, 0.091, 0.234, 0.594, 0.639, 1.738, 0.082, 0.665, 0.724, 0,
               3.607, 0, 0.05, 0.064, 6.68, 4.16, 7.3, 12, 12, 0]
vit_b12_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00004, 0.0005, 0.0016, 0.001, 0.007, 0.002, 0.004,
                0.0003, 0.032, 2]
vit_c_list = [5.9, 19.7, 7.4, 0, 0.3, 6, 6.3, 4.6, 36.6, 14, 89.2, 10, 0, 8.7, 28, 0, 2.1, 0, 0, 0, 0, 0, 0, 0, 33.8, 0]
vit_d_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.002, 0.080, 0.180, 0.001, 0.006, 0, 0.01, 0.002,
              0.0004, 10]
vit_k_list = [0.0132, 0.0019, 0, 0, 0, 0.047, 0.014, 0.002, 0.076, 0.008, 0.101, 0.021, 0, 0, 0.483, 0.06, 0, 0, 0.003,
              0.03, 0, 0, 0, 0, 0, 0]
A_eq = np.array([[173, 322, 166, 1418, 1361, 1866, 2629, 218, 103, 74, 141, 670, 1576, 371, 97,
                  3699, 93, 252, 1682, 647, 647, 787, 964, 621, 482, 0]])

A_ub = -1 * np.array(
    [protein_list, carbohydrate_list, fat_list, vit_a_list, vit_b1_list, vit_b2_list, vit_b3_list, vit_b12_list,
     vit_c_list, vit_d_list, vit_k_list], dtype="double")  # skapar matris med alla värden från listorna

b_ub = np.array([-60000, -275000, -70000, -0.7, -1.1, -1.2, -15, -0.002, -75, -0.01, -0.065])  # Näringsbehoven
b_eq = np.array([8710])  # Kaloribehov

result = sp.optimize.linprog(c=cost, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method='highs',
                                bounds=[0, None],
                                options={"primal_feasibility_tolerance": 1e-10})

# Maximerar kalorier och näringsvärden med linjär optimering (vi kollar på x-värdet för varje matvara där prioriteras
# högra siffror)

foods = ["Carrot", "Potato", "Onion", "Wheat flour", "Yeast(dry)", "Soy beans", "Hazelnuts", "Apple", "Cabbage",
         "Tomato", "Broccoli", "Avocado", "Brown sugar", "Bananas", "Spinach", "Olive oil", "Mushrooms", "Milk",
         "Cheddar", "Eggs", "Pork shoulder", "Ground beef", "Salmon filet", "Chicken meat", "Chicken Liver",
         'Vegan supplement']
print(result)
cost_total = 0
print("Ingredients for the perfect meal!")
for food in range(len(foods)):  # For loop printar alla matvaror som ska användas och hur mycket det kostar totalt
    if result.x[food] > 0:
        print(foods[food], ":", result.x[food], "hg", cost[food], "kr")
        cost_total += result.x[food] * cost[food]
print("Cost of perfect meal:", cost_total, "kr")