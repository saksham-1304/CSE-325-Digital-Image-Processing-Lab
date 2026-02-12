import numpy as np
import cv2
import matplotlib.pyplot as plt

# Create two grayscale images
img1 = np.zeros((256, 256), dtype=np.uint8)
img2 = np.zeros((256, 256), dtype=np.uint8)

img1[50:200, 50:200] = 255
img2[100:230, 100:230] = 255

# AND operation
and_img = cv2.bitwise_and(img1, img2)

# Display
plt.figure(figsize=(8, 3))
plt.subplot(1, 3, 1), plt.imshow(img1, cmap='gray'), plt.title("Image 1")
plt.subplot(1, 3, 2), plt.imshow(img2, cmap='gray'), plt.title("Image 2")
plt.subplot(1, 3, 3), plt.imshow(and_img, cmap='gray'), plt.title("AND Result")
plt.axis('off')
plt.show()
