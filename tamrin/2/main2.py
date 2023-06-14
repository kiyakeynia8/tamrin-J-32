import numpy as np 
import cv2

image=cv2.imread("input/1.tif",cv2.IMREAD_GRAYSCALE)

kernels = [np.ones((5,5))/40,np.ones((5,5)),np.ones((5,5))*5,np.ones((3,3))/40,np.ones((3,3)),np.ones((3,3))*5]
results = []

def result(kernel):
    results.append(cv2.filter2D(image,-1,kernel))

for i in range(6):
    result(kernels[i])

total_result = np.hstack((image,results[0],results[1],results[2],results[3],results[4],results[5]))

cv2.imwrite("output assignment_32/2_result.png",total_result)