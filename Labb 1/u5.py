from math import pi

n1 = 10
n2 = 100
n3 = 1000

# ------------------------------------------------------------

# n = 10
result1 = 0
for k in range(1, n1+1):
    result1 = result1 + 1/k**2
print("n=10: ", result1)

# Avvikelsen från pi^2/6 är:
print("Avvikelse:", pi**2/6 - result1)
print()

# ------------------------------------------------------------

# n = 100
result2 = 0
for k in range(1, n2+1):
    result2 = result2 + 1/k**2
print("n=100: ", result2)

# Avvikelsen från pi^2/6 är:
print("Avvikelse:", pi**2/6 - result2)
print()

# ------------------------------------------------------------

# n = 1000
result3 = 0
for k in range(1, n3+1):
    result3 = result3 + 1/k**2
print("n=1000: ", result3)

# Avvikelsen från pi^2/6 är:
print("Avvikelse:", pi**2/6 - result3)
print()

