# Convert a Color Image into Gray Scale Image
import cv2

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale Image", gray)
cv2.imwrite("gray.png", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Gray = 0.299R + 0.587G + 0.114B