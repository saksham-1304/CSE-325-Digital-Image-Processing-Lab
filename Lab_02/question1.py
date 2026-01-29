import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (6,6)
plt.rcParams['image.cmap'] = 'gray'

# --------------------------------------------------
# 1. Sampling and Quantization
# --------------------------------------------------
img = np.tile(np.linspace(0, 255, 256, dtype=np.uint8), (256,1))

sampled = img[::4, ::4]

levels = 8
quantized = np.floor(img / (256/levels)) * (256/levels)

plt.figure(figsize=(12,4))
plt.subplot(1,3,1); plt.title("Original"); plt.imshow(img)
plt.subplot(1,3,2); plt.title("Sampled"); plt.imshow(sampled)
plt.subplot(1,3,3); plt.title("Quantized"); plt.imshow(quantized)
plt.show()
