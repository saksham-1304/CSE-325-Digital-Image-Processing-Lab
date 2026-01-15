# Resize the Image by One Half and One Quarter

import cv2

img = cv2.imread("input.jpg")

half = cv2.resize(img, None, fx=0.5, fy=0.5)
quarter = cv2.resize(img, None, fx=0.25, fy=0.25)

cv2.imshow("Half Size", half)
cv2.imshow("Quarter Size", quarter)
cv2.imwrite("half.png", half)
cv2.imwrite("quarter.png", quarter)

cv2.waitKey(0)
cv2.destroyAllWindows()
