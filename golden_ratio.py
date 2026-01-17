import matplotlib.pyplot as plt
import numpy as np

PHI = (1 + np.sqrt(5)) / 2  # ≈ 1.618

# Golden triangle vertices (base = 1, height = φ/2 * base)
vertices = np.array([
    [0,          0],
    [1,          0],
    [0.5,  np.sqrt(PHI**2 - 0.25)]   # height for isosceles golden triangle
])

def golden_sierpinski(n_points=80000):
    point = np.array([0.5, 0.4])  # start roughly in center
    x, y = [point[0]], [point[1]]

    for _ in range(n_points):
        v = vertices[np.random.randint(0, 3)]
        point = (point + v) / 2
        x.append(point[0])
        y.append(point[1])

    plt.figure(figsize=(10, 10 * (np.sqrt(PHI**2 - 0.25))))  # preserve proportion
    plt.scatter(x, y, s=0.25, color='#2a2a6e', alpha=0.7, edgecolor='none')
    plt.axis('equal')
    plt.axis('off')
    plt.title("Golden Ratio Sierpiński Triangle (chaos game)", fontsize=13)
    plt.tight_layout()
    plt.show()

golden_sierpinski(120000)
