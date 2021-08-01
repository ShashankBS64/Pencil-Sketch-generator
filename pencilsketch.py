import os
import cv2

os.chdir('Directory to fetch the source image from')

image = cv2.imread("image_name")
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_img = 255 - gray_img
blurred = cv2.GaussianBlur(inverted_img, (31,31), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_img, inverted_blurred, scale=256.0)

cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)


