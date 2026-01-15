# Convert the Color Image into Binary Image
import cv2

img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary conversion
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary Image", binary)
cv2.imwrite("binary.png", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
