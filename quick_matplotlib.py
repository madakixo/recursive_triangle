import matplotlib.pyplot as plt
import numpy as np

def sierpinski_points(iterations=8, points=80000):
    # Starting points of big triangle
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    
    # Start somewhere inside
    point = np.array([0.5, 0.5])
    x, y = [point[0]], [point[1]]
    
    for _ in range(points):
        # Choose random vertex
        v = vertices[np.random.randint(0, 3)]
        # Move halfway towards it
        point = (point + v) / 2
        x.append(point[0])
        y.append(point[1])
    
    plt.figure(figsize=(10,10))
    plt.scatter(x, y, s=0.3, color='midnightblue', alpha=0.7)
    plt.axis('equal')
    plt.axis('off')
    plt.title(f"Sierpiński Triangle – {iterations} iterations (chaos game)", fontsize=14)
    plt.tight_layout()
    plt.show()

sierpinski_points(iterations=9, points=120000)
