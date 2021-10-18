import cv2
# import numpy as np

img = cv2.imread("teste1.jpg", cv2.IMREAD_GRAYSCALE)

surf = cv2.xfeatures2d.SURF_create()

# kp = sift.detect(img, None)
keypoints, descriptors = surf.detectAndCompute(img, None)

img = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
