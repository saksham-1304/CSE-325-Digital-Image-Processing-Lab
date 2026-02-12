import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# PARAMETERS
# -------------------------------
IMAGE_SIZE = 1024
LINE_SIZE = 128
BLACK = 0
WHITE = 255

# -------------------------------
# IMAGE A: HORIZONTAL STRIPES
# -------------------------------
image_A = np.zeros((IMAGE_SIZE, IMAGE_SIZE), dtype=np.uint8)

for i in range(0, IMAGE_SIZE, LINE_SIZE):
    if (i // LINE_SIZE) % 2 == 0:
        image_A[i:i+LINE_SIZE, :] = WHITE
    else:
        image_A[i:i+LINE_SIZE, :] = BLACK

# -------------------------------
# IMAGE B: VERTICAL STRIPES
# -------------------------------
image_B = np.zeros((IMAGE_SIZE, IMAGE_SIZE), dtype=np.uint8)

for j in range(0, IMAGE_SIZE, LINE_SIZE):
    if (j // LINE_SIZE) % 2 == 0:
        image_B[:, j:j+LINE_SIZE] = WHITE
    else:
        image_B[:, j:j+LINE_SIZE] = BLACK

# -------------------------------
# ARITHMETIC OPERATIONS
# -------------------------------

# Convert to int for safe arithmetic
A = image_A.astype(np.int16)
B = image_B.astype(np.int16)

# (a) ADDITION
add_AB = np.clip(A + B, 0, 255).astype(np.uint8)

# (b) SUBTRACTION
sub_AB = np.clip(A - B, 0, 255).astype(np.uint8)

# (c) MULTIPLICATION (normalize by 255)
mul_AB = np.clip((A * B) // 255, 0, 255).astype(np.uint8)

# (d) AVERAGING
avg_AB = np.clip((A + B) // 2, 0, 255).astype(np.uint8)

# -------------------------------
# DISPLAY RESULTS
# -------------------------------
titles = [
    "Image A (Horizontal Stripes)",
    "Image B (Vertical Stripes)",
    "Addition (A + B)",
    "Subtraction (A - B)",
    "Multiplication (A × B)",
    "Averaging (A + B) / 2"
]

images = [
    image_A,
    image_B,
    add_AB,
    sub_AB,
    mul_AB,
    avg_AB
]

plt.figure(figsize=(12, 8))

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

# -------------------------------
# SAVE OUTPUT IMAGES
# -------------------------------
plt.imsave("Image_A_horizontal.png", image_A, cmap='gray')
plt.imsave("Image_B_vertical.png", image_B, cmap='gray')
plt.imsave("Addition_AB.png", add_AB, cmap='gray')
plt.imsave("Subtraction_AB.png", sub_AB, cmap='gray')
plt.imsave("Multiplication_AB.png", mul_AB, cmap='gray')
plt.imsave("Average_AB.png", avg_AB, cmap='gray')

print("All images generated and saved successfully.")

