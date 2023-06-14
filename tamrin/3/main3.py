import cv2
import numpy as np

# image = cv2.imread("input/board_noisy.png", 0)

# image = cv2.imread("input/Capture (2).PNG", 0)

image = cv2.imread("input/balloons_noisy.png")

# image = cv2.imread("input/Medianfilterp.png", 0)

# image = cv2.imread("input/5.png")

for i in range(5):
    result = cv2.medianBlur(image,3)

    # cv2.imwrite("output assignment_32/3_result_1.png", result)
    # image = cv2.imread("output assignment_32/3_result_1.png", 0)

    # cv2.imwrite("output assignment_32/3_result_2.png", result)
    # image = cv2.imread("output assignment_32/3_result_2.png", 0)

    cv2.imwrite("output assignment_32/3_result_3.png", result)
    image = cv2.imread("output assignment_32/3_result_3.png")

    # cv2.imwrite("output assignment_32/3_result_4.png", result)
    # image = cv2.imread("output assignment_32/3_result_4.png")

    # cv2.imwrite("output assignment_32/3_result_5.png", result)
    # image = cv2.imread("output assignment_32/3_result_5.png")