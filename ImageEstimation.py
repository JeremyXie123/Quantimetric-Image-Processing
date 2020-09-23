import cv2
import numpy as np

# image estimation of v12 from v11 from part 4 of the lab

def g_func(array):
    slope = [1.1860, 1.1873, 1.1873]
    shift = [2.8291, 3.1441, 3.0909]
    return np.add(np.multiply(array,slope),shift)

if __name__=="__main__":
    image1 = cv2.imread("Stills/v11.jpg")

    image1 = np.apply_along_axis(g_func, 2, image1)

    print("done")
    cv2.imwrite("v12fromv11.jpg",image1)
