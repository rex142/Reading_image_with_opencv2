import cv2 as cv
import sys


# reading image from storage
img = cv.imread("cat.jpg")

# resizign the image now

# returns a resized image doesnt modify the og image.
img_resized = cv.resize(img, (400, 400))

# if image isnt available

if img is None:
    sys.exit("couldn't read the image")

# displaying the image

cv.imshow("displaying Cat", img_resized)
cv.waitKey(0)  # wait infintly till the user press any key only then exit

# issue : image was too big for screen size so did a stackoverflow search


#
