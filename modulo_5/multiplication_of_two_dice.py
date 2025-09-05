results = [randint(1, 6) * randint(1, 6) for _ in range(1000)]

plt.hist(results, bins=range(1, 37), edgecolor='black')
plt.title("Multiplication of Two D6 Rolls")
plt.xlabel("Product")
plt.ylabel("Frequency")
plt.show()
