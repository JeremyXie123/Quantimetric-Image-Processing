import cv2
import numpy as np
from math import log

#Constants derived from part 3 of the lab.
GAMMA = [0.2461, 0.2476, 0.2477]
ALPHA = [-15.2087, -16.7896, -16.4996]
BETA = [1, 1, 1]
k_a = [1.1860, 1.1873, 1.1873]
k_b = [2.8291, 3.1441, 3.0909]
DT = 0.1
k_exp = 2

def v(fxy, alpha, a):
    # calculates the sample function for evaluating the derivative
    return log(f_inv(fxy,alpha,a))


def f_inv(fxy, alpha, a):
    # pow(fxy-alpha, 1/a)
    return pow(fxy - alpha, 1 / a)


def certainty(fxy, alpha, a):
    # Calculate the symmetrical derivative at the given point
    return (2*DT)/(v(fxy+DT, alpha, a)-v(fxy-DT, alpha, a))


def calculate_q(fxy, alpha, a, k_exp):
    return f_inv(fxy, alpha, a) * 1 / k_exp


def pixel_cert(rgb):
    # returns the certainty pixel given a pixel
    r = certainty(rgb[0], ALPHA[0], k_a[0])
    g = certainty(rgb[1], ALPHA[1], k_a[1])
    b = certainty(rgb[2], ALPHA[2], k_a[2])
    return [r, g, b]


def pixel_calc_q(rgb):
    # returns the value of q given a pixel
    r = calculate_q(rgb[0], ALPHA[0], k_a[0], k_exp)
    g = calculate_q(rgb[1], ALPHA[1], k_a[1], k_exp)
    b = calculate_q(rgb[2], ALPHA[2], k_a[2], k_exp)
    return [r, g, b]


def weight_image(image):
    # apply the certainty function for all pixels and return it

    output = np.apply_along_axis(pixel_cert, 2, image)
    return output


def certainty_image(image, weight):
    # apply calculate q for all pixels and return it, then apply the certainty image

    output = np.apply_along_axis(pixel_calc_q, 2, image) * weight
    return output


if __name__ == "__main__":
    names = ["v01", "v02", "v03", "v04"]

    # blank image with no data
    #stores the certainty images
    numerator = np.empty([1080, 1920, 3], dtype="float")

    #stores the certainty weights
    denominator = np.empty([1080, 1920, 3], dtype="float")

    for index, name in enumerate(names):
        k_exp = 2 ** (index)
        image = cv2.imread("Stills/"+name+".jpg")
        print(name, image.shape)
        weight = weight_image(image)
        cert_img = certainty_image(image, weight)

        numerator += cert_img
        denominator += weight

    image = numerator / denominator
    image = image.astype("uint8")
    cv2.imwrite("antihomomorphic.jpg", image)