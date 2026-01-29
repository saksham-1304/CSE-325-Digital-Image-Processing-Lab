import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (6,6)
plt.rcParams['image.cmap'] = 'gray'
# --------------------------------------------------
# 2. Distance Measures
# --------------------------------------------------
p1 = (200,300)
p2 = (700,900)

dx = abs(p1[0] - p2[0])
dy = abs(p1[1] - p2[1])

De = np.sqrt(dx**2 + dy**2)
D4 = dx + dy
D8 = max(dx, dy)

print("Euclidean Distance (De):", De)
print("City-block Distance (D4):", D4)
print("Chessboard Distance (D8):", D8)
