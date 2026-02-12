import numpy as np
import matplotlib.pyplot as plt

# Create a white image (255)
image = np.ones((256, 256), dtype=np.uint8) * 255

# Size of black box
box_size = 58

# Calculate center position
start = (256 - box_size) // 2
end = start + box_size

# Insert black box (0 intensity)
image[start:end, start:end] = 0

# Display image
plt.imshow(image, cmap='gray')
plt.title("White Image with Black Center Box (58x58)")
plt.axis('off')
plt.show()
