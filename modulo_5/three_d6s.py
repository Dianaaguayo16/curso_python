results = [randint(1, 6) + randint(1, 6) + randint(1, 6) for _ in range(1000)]

plt.hist(results, bins=range(3, 19), edgecolor='black')
plt.title("Results of Rolling Three D6s")
plt.xlabel("Sum")
plt.ylabel("Frequency")
plt.show()
