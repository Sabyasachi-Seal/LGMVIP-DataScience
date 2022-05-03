import cv2
image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)
invertedimage = 255 - gray_image
cv2.imshow("Inverted Image", invertedimage)
cv2.waitKey(0)
blurred = cv2.GaussianBlur(invertedimage, (21, 21), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
inverted_blurred = 255 - blurred
pencilsketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Pencil Sketch", pencilsketch)
cv2.waitKey(0)