import matplotlib.pyplot as plt

# First 5 cubes
x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.figure(figsize=(6, 4))
plt.plot(x_values, y_values, marker='o')
plt.title("First 5 Cubic Numbers")
plt.xlabel("Value")
plt.ylabel("Cube")
plt.show()

# First 5000 cubes
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, s=1)
plt.title("First 5000 Cubic Numbers")
plt.xlabel("Value")
plt.ylabel("Cube")
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, c=y_values, cmap='viridis', s=1)
plt.title("Colored Cubes with Colormap")
plt.xlabel("Value")
plt.ylabel("Cube")
plt.colorbar()
plt.show()
