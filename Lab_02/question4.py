import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (6,6)
plt.rcParams['image.cmap'] = 'gray'

# --------------------------------------------------
# 4. Intensity & Bit Plane Slicing
# --------------------------------------------------
img=cv2.imread("input.jpg")  
low, high = 100, 150
intensity_slice = np.where((img >= low) & (img <= high), 255, 0)

bit_planes = [(img >> i) & 1 for i in range(8)]

plt.figure(figsize=(12,6))
plt.subplot(2,4,1); plt.title("Original"); plt.imshow(img)
plt.subplot(2,4,2); plt.title("Intensity Slice"); plt.imshow(intensity_slice)

for i in range(6):
    plt.subplot(2,4,3+i)
    plt.title(f"Bit {i}")
    plt.imshow(bit_planes[i]*255)
plt.show()
