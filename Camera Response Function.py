import numpy as np
import cv2
from math import log
from Comparagram import image_to_channels

def line_of_best_fit(image1,image2):
    image1_channels = image_to_channels(image1)
    image2_channels = image_to_channels(image2)

    channel_count = len(image1_channels)
    equations = [[None,None] for i in range(3)]

    for index in range(channel_count):
        # deriving the line of best fit from a color channel
        poly = np.polyfit(image1_channels[index], image2_channels[index], 1)
        equations[index][0] = poly[0]
        equations[index][1] = poly[1]

    return equations

if __name__=="__main__":
    # initialize slope variables
    # The equations will be stored in an array of 3 rows by 2 columns
    # with each row denoting the color channel and each column denoting
    # the coefficient of the regressed line's slope and vertical shift.

    g_funcs = [[0.0,0.0] for i in range(3)]

    names = ["v01","v02","v03","v04","v05","v06","v07","v08","v09","v10","v11","v12"]
    count = 0
    for i in range(len(names)-1):
        # iterating through the images from v01-v12
        name1 = names[i]
        name2 = names[i+1]

        image1 = cv2.imread("Stills/"+name1+".jpg")
        image2 = cv2.imread("Stills/"+name2+".jpg")

        equations = line_of_best_fit(image1,image2)
        for i in range(3):
            g_funcs[i][0] = g_funcs[i][0] + equations[i][0]
            g_funcs[i][1] = g_funcs[i][1] + equations[i][1]

        # print(equations)
        count += 1
    # slope averaging
    for i in range(3):
        g_funcs[i][0] = g_funcs[i][0] / count
        g_funcs[i][1] = g_funcs[i][1] / count

    for index, color in enumerate(["r","g","b"]):
        # derivation of f(q) from the coefficients of the line of best fit
        slope = g_funcs[index][0]
        shift = g_funcs[index][1]
        gamma = log(slope,2)

        alpha = shift/(1-slope)
        beta = 1
        print("Channel {}: g = {:.4f}f + {:.4f}, \u03B3 = {:.4f}, f = {:.4f} + {:.4f}q ^ {:.4f}".format(color, slope, shift, gamma, alpha, beta, gamma))

'''
r g(x) = 1.2271613845654041f 1.4831723589977548
g g(x) = 1.2294615363060106f 1.4205045046732352
b g(x) = 1.2256689629721547f 1.520333938661079
'''