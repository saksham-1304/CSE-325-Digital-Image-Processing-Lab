import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (6,6)
plt.rcParams['image.cmap'] = 'gray'

# --------------------------------------------------
# 3. Negation, Log & Power Law
# --------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Create synthetic grayscale image
img = np.tile(np.linspace(0, 255, 256, dtype=np.uint8), (256,1))

# Normalize image for power-law transformation
img_norm = img / 255.0

# -------------------------------
# Image Negation
# -------------------------------
negative = 255 - img

# -------------------------------
# Log Transformation
# -------------------------------
c = 255 / np.log(1 + np.max(img))
log_img = c * np.log(1 + img)
log_img = log_img.astype(np.uint8)

# -------------------------------
# Power-Law (Gamma) Transformation
# -------------------------------
gamma_values = [0, 0.5, 1, 2]
power_imgs = [(img_norm ** g) for g in gamma_values]

# -------------------------------
# Display Results
# -------------------------------
plt.figure(figsize=(14,6))

plt.subplot(2,4,1)
plt.title("Original")
plt.imshow(img, cmap='gray')

plt.subplot(2,4,2)
plt.title("Negative")
plt.imshow(negative, cmap='gray')

plt.subplot(2,4,3)
plt.title("Log Transform")
plt.imshow(log_img, cmap='gray')

for i, g in enumerate(gamma_values):
    plt.subplot(2,4,5+i)
    plt.title(f"Gamma = {g}")
    plt.imshow(power_imgs[i], cmap='gray')

plt.show()