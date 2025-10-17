import matplotlib.pyplot as plt

# Define the points
points = [(1, 3), (2, 10), (6, 12), (18, 20)]

# Separate x and y values
x_values, y_values = zip(*points)

# Plot the red line
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, color='red', linestyle='-', linewidth=2)

# Plot green points
plt.scatter(x_values, y_values, color='green', s=100, zorder=5)

# Annotate points
for x, y in points:
    plt.text(x, y + 0.7, f'({x},{y})', ha='center')


plt.title('Line Through Given Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.tight_layout()
plt.show()
