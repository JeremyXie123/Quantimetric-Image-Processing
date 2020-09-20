import cv2
import numpy as np

def g_func(array):
    slope = [1.1860, 1.1873, 1.1873]
    shift = [2.8291, 3.1441, 3.0909]
    return np.add(np.multiply(array,slope),shift)

if __name__=="__main__":
    image1 = cv2.imread("Stills/v11.jpg")
    print(image1.shape)
    columns = image1.shape[0]
    rows = image1.shape[1]
    channels = image1.shape[2]

    image1 = np.apply_along_axis(g_func, 2, image1)

    print("done")
    cv2.imwrite("v12fromv11.jpg",image1)
