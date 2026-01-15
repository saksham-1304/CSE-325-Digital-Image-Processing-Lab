# Rotate the Image by 45°, 90° and 180°

import cv2

img = cv2.imread("input.jpg")
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# Rotate 45 degrees
M45 = cv2.getRotationMatrix2D(center, 45, 1.0)
rot45 = cv2.warpAffine(img, M45, (w, h))

# Rotate 90 degrees
rot90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Rotate 180 degrees
rot180 = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow("45 Degree Rotation", rot45)
cv2.imshow("90 Degree Rotation", rot90)
cv2.imshow("180 Degree Rotation", rot180)

cv2.imwrite("rot45.png", rot45)
cv2.imwrite("rot90.png", rot90)
cv2.imwrite("rot180.png", rot180)

cv2.waitKey(0)
cv2.destroyAllWindows()
