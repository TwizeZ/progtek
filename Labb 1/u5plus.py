import math

n1 = 10
n2 = 100
n3 = 1000


def sum(n):
    result = 0
    for n in range(1, n+1):
        result = result + 1/n**2
    return result


print("n=10: ", sum(n1))
print("n=100: ", sum(n2))
print("n=1000: ", sum(n3))
print("n=∞:", math.pi**2/6, "((pi^2)/6)")

# Ju större n är, desto närmare kommer summan att komma pi^2/6.