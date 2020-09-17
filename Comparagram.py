import cv2
import numpy as np
import matplotlib.pyplot as plt


def image_to_channels(image):
    shape = image.shape
    channel_count = shape[2]
    channels = [None for i in range(channel_count)]
    for i in range(channel_count):
        channels[i] = image[:, :, i].flatten()
    return channels


def comparagram_plot(image1, image2, regress, monochrome, axises, labels, save, path):
    # convert images into their respective color channels
    image1_channels = image_to_channels(image1)
    image2_channels = image_to_channels(image2)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # monotone/colored differentiation colors
    if monochrome:
        colors = ["black", "black", "black"]
        # ax.set_facecolor((0, 0 0))
    else:
        colors = ["r", "g", "b"]

        # RGB
    for index, color in enumerate(colors):
        ax.scatter(image1_channels[index], image2_channels[index], s=0.3, c=color)

    if regress:
        samples = np.linspace(0,256, 2)
        for index, color in enumerate(colors):
            poly = np.polyfit(image1_channels[index],image2_channels[index],1)
            #print(color,"g(x) = "+str(poly[0])+"f"+" "+str(poly[1]))
            plt.plot(samples,poly[0]*samples+poly[1],"-")


    ax.set_aspect('equal', adjustable='box')
    plt.axis('square')

    # axis visibility
    if not axises:
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)

    # Labels
    if labels:
        plt.ylabel('Image 2 [g(f)]')
        plt.xlabel('Image 1 [f]')
        ax.set_title("Comparagram")

    ax.set(xlim=(0, 256), ylim=(0, 256))

    # Export/Viewing
    if save:
        plt.savefig(path, bbox_inches='tight')
    else:
        plt.show()


if __name__ == "__main__":
    names = ["v01","v02","v03","v04","v05","v06","v07","v08","v09","v10","v11","v12"]
    count = 0
    for i in range(len(names)-1):
        # iterating through the images from v01-v12
        name1 = names[i]
        name2 = names[i+1]

        image1 = cv2.imread("Stills/"+name1+".jpg")
        image2 = cv2.imread("Stills/"+name2+".jpg")

        comparagram_plot(image1, image2, True, False, True, True, True, "Comparagrams/{}-{}.png".format(name1,name2))
    print("Process Finished")
