import cv2
import numpy as np
imageName = input("Please enter the name of your image:\n")
print("Processing...")
try:
  img = cv2.imread(imageName)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
except:
  print("File does not exit")
  exit(0)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Cartoon", cartoon)
print("Done.")
cv2.waitKey(0)
cv2.destroyAllWindows()