import cv2

# part 2 of lab (video signal averaging)

def video_to_images(video):
    vidcap = cv2.VideoCapture(video)
    images = []
    while True:
        ret, frame = vidcap.read()
        if ret:
            #if we can still read
            images.append(frame)
        else:
            return images

def average_images(images):
    count = len(images)
    output = images[0]
    for i in range(1,count):
        image = images[i]
        image = image.astype("float")
        output = output + image
    output = output / count
    output = output.astype("uint8")
    return output

if __name__=="__main__":
    names = ["v01", "v02", "v03", "v04", "v05", "v06", "v07", "v08", "v09", "v10", "v11", "v12"]
    for name in names:
        # separate the video into multiple images
        images = video_to_images(name+".mp4")
        # slice off first and last images
        images = images[1:len(images)-1]
        # average the images
        image = average_images(images)
        # output the image
        cv2.imwrite(name+".jpg", image)

