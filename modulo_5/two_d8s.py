from random import randint
import matplotlib.pyplot as plt

results = [randint(1, 8) + randint(1, 8) for _ in range(1000)]

plt.hist(results, bins=range(2, 17), edgecolor='black')
plt.title("Results of Rolling Two D8s 1000 Times")
plt.xlabel("Sum")
plt.ylabel("Frequency")
plt.show()
