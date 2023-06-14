import cv2

# image_low_contrast = cv2.imread("input/4.png",0)
image_low_contrast = cv2.imread("input/Unequalized_Hawkes_Bay_NZ.jpg",0)

image_high_contrast = cv2.equalizeHist(image_low_contrast)
# cv2.imwrite("output assignment_32/4_result_1.png", image_high_contrast)
cv2.imwrite("output assignment_32/4_result_2.png", image_high_contrast)