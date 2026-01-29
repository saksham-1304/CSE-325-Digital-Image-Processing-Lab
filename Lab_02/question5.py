import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (6,6)
plt.rcParams['image.cmap'] = 'gray'


# --------------------------------------------------
# 5. Contrast Stretching
# --------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Create synthetic low-contrast image
img = np.tile(np.linspace(80, 160, 256, dtype=np.uint8), (256,1))

# Contrast Stretching
r_min = img.min()
r_max = img.max()

stretched = (img - r_min) * (255 / (r_max - r_min))
stretched = stretched.astype(np.uint8)

# Display images
plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.title("Original Synthetic Image")
plt.imshow(img, cmap='gray')

plt.subplot(1,3,2)
plt.title("Contrast Stretched Image")
plt.imshow(stretched, cmap='gray')

# Histogram comparison
plt.subplot(1,3,3)
plt.title("Histogram Comparison")
plt.hist(img.ravel(), 256, [0,256], alpha=0.5, label="Original")
plt.hist(stretched.ravel(), 256, [0,256], alpha=0.5, label="Stretched")
plt.legend()

plt.show()