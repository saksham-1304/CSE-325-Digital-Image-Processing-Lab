import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (6,6)
plt.rcParams['image.cmap'] = 'gray'

# --------------------------------------------------
# 6. Histogram Equalization
# --------------------------------------------------
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Create synthetic grayscale image (low contrast)
img = np.tile(np.linspace(50, 180, 256, dtype=np.uint8), (256,1))

# Apply histogram equalization
equalized = cv2.equalizeHist(img)

# Display images
plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.title("Original Synthetic Image")
plt.imshow(img, cmap='gray')

plt.subplot(1,3,2)
plt.title("Histogram Equalized Image")
plt.imshow(equalized, cmap='gray')

# Plot histograms
plt.subplot(1,3,3)
plt.title("Histogram Comparison")
plt.hist(img.ravel(), 256, [0,256], alpha=0.5, label="Original")
plt.hist(equalized.ravel(), 256, [0,256], alpha=0.5, label="Equalized")
plt.legend()

plt.show()

