import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# a

a = np.array([[4, -1, -9, -4, -6], [1, 1, -1, 4, -5], [0, -3, 4, 7, 0], [3, -5, -5, -3, 7], [9, -1, 4, -8, -9]])
b = np.array([-59, -21, 20, 16, -11])
x = np.linalg.solve(a, b)

print("x1:", x.item(0), "x2:", x.item(1), "x3:", x.item(2),"x4: ", x.item(3), "x5:", x.item(4))

# b

def price(file_name):
    with open(file_name, "r", encoding="utf8") as file:
        price_list = []
        for i, line in enumerate(file):
            if i < 2:
                continue
            elements = line.split()
            price_list.append(float(elements[1]))
        return price_list


def kilometres(file_name):
    with open(file_name, "r", encoding="utf8") as file:
        kilometres_list = []
        for i, line in enumerate(file):
            if i < 2:
                continue
            elements = line.split()
            kilometres_list.append(float(elements[2]))
        return kilometres_list


file = "Shinkansen.text"
x = np.array(kilometres(file))
y = np.array(price(file))

print()
print(x)
print(y)

A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.show()

def price_2(x):
    return m*x + c

print(f"\nSendai - Tokyta: {price_2(325.4)} JPY")
print(f"Stockholm - Göteborg: {price_2(455)*0.07} SEK\n")
print("\n---\n")

# c

def read_nutrients(file_name):
    nutrients_dict = {}
    with open(file_name, "r", encoding="utf8") as file:
        for i, line in enumerate(file):
            if line == "\n" or line == "":
                break

            if i < 2:
                continue

            elements = line.split()
            for item in elements:
                item.replace(" ", "")
            
            nutrients_dict[elements[0]] = {"protein":float(elements[1]),
                                      "carbonhydrates":float(elements[2]),
                                      "fat":float(elements[3]),
                                      "A":float(elements[4]),
                                      "B1":float(elements[5]),
                                      "B2":float(elements[6]),
                                      "B3":float(elements[7]),
                                      "B12":float(elements[8]),
                                      "C":float(elements[9]),
                                      "D":float(elements[10]),
                                      "K":float(elements[11]),
                                      "energy":float(elements[12]),
                                      "price":float(elements[13])}        
        return nutrients_dict


def read_behov(file_name):
    behov_list = []
    with open(file_name, "r", encoding="utf8") as file:
        line = file.readlines()[-1]
        elements = line.split()
        for item in elements:
            behov_list.append(float(item[:-1]))
        
        return behov_list


behov = read_behov("Naringsbehov.text")
nutrients = read_nutrients("nutrients.text")

foods = [x[:-1] for x in list(nutrients.keys())]
proteins = []
carbonhydrates = []
fats = []
vit_a = []
vit_b1 = []
vit_b2 = []
vit_b3 = []
vit_b12 = []
vit_c = []
vit_d = []
vit_k = []
energies = []
prices = []

for _, value in nutrients.items():
    proteins.append(value["protein"])
    carbonhydrates.append(value["carbonhydrates"])
    fats.append(value["fat"])
    vit_a.append(value["A"])
    vit_b1.append(value["B1"])
    vit_b2.append(value["B2"])
    vit_b3.append(value["B3"])
    vit_b12.append(value["B12"])
    vit_c.append(value["C"])
    vit_d.append(value["D"])
    vit_k.append(value["K"])
    energies.append(value["energy"])
    prices.append(value["price"])

cost = np.array(prices)
A_ub = -1 * np.array([proteins, carbonhydrates, fats, vit_a, vit_b1, vit_b2, vit_b3, vit_b12, vit_c, vit_d, vit_k], dtype="double")
A_eq = np.array([energies])
b_ub = -1 * np.array(behov)
b_eq = np.array([8710])

result = sp.optimize.linprog(c=cost, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method='highs', bounds=[0, None], options={"primal_feasibility_tolerance": 1e-10})
print(result)

tot_cost = 0
for food in range(len(foods)):
    if result.x[food] > 0:
        print(f"{foods[food]}: {result.x[food]} hg, {cost[food]} kr")
        tot_cost += result.x[food] * cost[food]
print(f"Cost of perfect meal: {tot_cost} kr")