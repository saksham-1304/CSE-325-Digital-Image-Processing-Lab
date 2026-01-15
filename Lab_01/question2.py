#Find RED, GREEN and BLUE Planes of a Color Image

import cv2

img = cv2.imread("input.jpg")

# Split channels
b, g, r = cv2.split(img)

cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

cv2.imwrite("blue_channel.png", b)
cv2.imwrite("green_channel.png", g)
cv2.imwrite("red_channel.png", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
