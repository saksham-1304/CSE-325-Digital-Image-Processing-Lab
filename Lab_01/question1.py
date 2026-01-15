# Read, Display and Write a Color Image in Various Formats (.jpg, .png, .tiff)

import cv2

# Read image
img = cv2.imread("input.jpg")

# Display image
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Write image in different formats
cv2.imwrite("output.png", img)
cv2.imwrite("output.tiff", img)
cv2.imwrite("output.jpg", img)
