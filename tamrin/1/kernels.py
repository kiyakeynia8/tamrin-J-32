import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input/bear.jpg",0)

mask = np.array([[-1, -1, -1],
                 [-1, 8, -1],
                 [-1, -1, -1]])

# mask = np.array([[0, -1, 0],
#                  [-1, 5, -1],
#                  [0, -1, 0]])

# mask = np.array([[-2, -1, 0],
#                  [-1,  1, 1],
#                  [ 0,  1, 2]])

# mask = np.array([[0, 0, 0],
#                  [0, 1, 0],
#                  [0, 0, 0]])

# mask = np.array([[-2, 1, 2],
#                  [-3, 2, 3],
#                  [-5, 1, 5]])

rows ,cols = image.shape
result = np.zeros(image.shape)

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_img = image[i-1:i+2 , j-1:j+2]
        result[i, j] = np.sum(small_img * mask)

result = np.hstack((image, result))

cv2.imwrite("output assignment_32/1_result_1.png",result)
# cv2.imwrite("output assignment_32/1_result_2.png",result)
# cv2.imwrite("output assignment_32/1_result_3.png",result)
# cv2.imwrite("output assignment_32/1_result_4.png",result)
# cv2.imwrite("output assignment_32/1_result_5.png",result)