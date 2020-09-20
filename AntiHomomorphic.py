import cv2
import numpy as np

K_EXP = 2
GAMMA = 1
ALPHA = [1,1,1]
BETA = [1,1,1]

def f(q):
    return 1

def f_inv(q):
    return 1


def calculate_q(value):
    return f_inv(value) * 1 / (K_EXP**2)

if __name__=="__main__":
    names = ["v01", "v02", "v03", "v04", "v05", "v06", "v07", "v08", "v09", "v10", "v11", "v12"]

    #blank image with no data
    total_sum = np.empty([1080,1920,3], dtype="uint8")
    for name in names:
        image = cv2.imread(name)
        converted = calculate_q(image)
