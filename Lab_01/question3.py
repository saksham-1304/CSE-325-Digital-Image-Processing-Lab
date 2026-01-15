#Create a Color Image from its RED, GREEN and BLUE Planes

import cv2

img = cv2.imread("input.jpg")

b, g, r = cv2.split(img)

# Merge channels
merged_img = cv2.merge((b, g, r))

cv2.imshow("Merged Color Image", merged_img)
cv2.imwrite("merged.png", merged_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
