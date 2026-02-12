import numpy as np
import cv2
import matplotlib.pyplot as plt

# Create grayscale image
img = np.zeros((256, 256), dtype=np.uint8)
img[60:190, 60:190] = 255

# NOT operation
not_img = cv2.bitwise_not(img)

plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title("Original Image")
plt.subplot(1, 2, 2), plt.imshow(not_img, cmap='gray'), plt.title("NOT Result")
plt.axis('off')
plt.show()
