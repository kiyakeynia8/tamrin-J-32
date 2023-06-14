import cv2
import matplotlib.pyplot as plt

image = cv2.imread("input/tsukuba_l.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("output assignment_32/5_result.png", image)