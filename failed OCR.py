import pytesseract
from PIL import Image
import cv2
import numpy as np

        #####  START PROGRAM - Read in photo, preprocess photo (cv2 - make =
machine readable), convert image to text (pytesseract)

            # NOTES
            # Remaining Factors:
            # Rotation and Skew of Image - (document scanner)
            # label being read horizontally, switch orientation
            # pictures are (horizontal), labels are positioned (horizontal)=
, pc will
            #
            # Reading [numbers] only, don't capture text



image_file =3D "IMG_0001.jpg"                   # load 1 desired image as i=
mage_file
img =3D cv2.imread(image_file)                  # # look into later - folde=
r or dropbox


# ALL USER DEF FUNCTION ---------------------------------------------------=
------------------------------------


##### copied online
# Change to grayscale, then black and white
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Get the image skew angle
def getSkewAngle(cvImage) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage =3D cvImage.copy()
    gray =3D cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur =3D cv2.GaussianBlur(gray, (9, 9), 0)
    thresh =3D cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRE=
SH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, can=
celling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks=
 of text
    kernel =3D cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate =3D cv2.dilate(thresh, kernel, iterations=3D2)

    # Find all contours
    contours, hierarchy =3D cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHA=
IN_APPROX_SIMPLE)
    contours =3D sorted(contours, key =3D cv2.contourArea, reverse =3D True=
)
    for c in contours:
        rect =3D cv2.boundingRect(c)
        x,y,w,h =3D rect
        cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)

    # Find largest contour and surround in min area box
    largestContour =3D contours[0]
    print (len(contours))
    minAreaRect =3D cv2.minAreaRect(largestContour)
    cv2.imwrite("temp/boxes.jpg", newImage)
    # Determine the angle. Convert it to the value that was originally used=
 to obtain skewed image
    angle =3D minAreaRect[-1]
    if angle < -45:
        angle =3D 90 + angle
    return -1.0 * angle
# Rotate the image around its center
def rotateImage(cvImage, angle: float):
    newImage =3D cvImage.copy()
    (h, w) =3D newImage.shape[:2]
    center =3D (w // 2, h // 2)
    M =3D cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage =3D cv2.warpAffine(newImage, M, (w, h), flags=3Dcv2.INTER_CUBI=
C, borderMode=3Dcv2.BORDER_REPLICATE)
    return newImage
# Deskew image
def deskew(cvImage):
    angle =3D getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)
# Remove Borders - copied online
def remove_borders(image):
    contours, heiarchy =3D cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.C=
HAIN_APPROX_SIMPLE)
    cntsSorted =3D sorted(contours, key=3Dlambda x:cv2.contourArea(x))
    cnt =3D cntsSorted[-1]
    x, y, w, h =3D cv2.boundingRect(cnt)
    crop =3D image[y:y+h, x:x+w]
    return (crop)
# thin out the font -
def thin_font(image):
    import numpy as np
    image =3D cv2.bitwise_not(image)
    kernel =3D np.ones((2,2),np.uint8)
    image =3D cv2.erode(image, kernel, iterations=3D1)
    image =3D cv2.bitwise_not(image)
    return (image)
##### -

# END USER DEF FUNCTIONS --------------------------------------------------=
------------------------------------
# PRE PROCESSING OPERATIONS FOR IMAGE -------------------------------------=
------------------------------------

# 1st Operation on image - grayscale -> black and white
gray =3D grayscale(img)
thresh, im_bw =3D cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)  #127 25=
5 - # 200, 255

# 2nd Operation on image - remove borders
noBorderImg =3D remove_borders(im_bw)
cv2.imwrite("temp/noBorders.jpg", noBorderImg)

# 3rd Operation - thin font
thinImg =3D thin_font(noBorderImg)
cv2.imwrite("temp/thin.jpg", thinImg) ##

# Last Operation? - Rotation and Skewing of Image
testImg =3D cv2.imwrite("temp/testImg.jpg", thinImg) ##
newImg =3D cv2.imread("temp/testImg.jpg")
fixed =3D deskew(newImg)
cv2.imwrite("temp/testFixed.jpg", fixed) ##
# Display Final Image in window
cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("win", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN=
)
cv2.imshow("win", fixed) ##
cv2.waitKey(0)



# END OF PREPROCESSING IMAGE ----------------------------------------------=
------------------------------------
# PYTESSERACT AND OCR BELOW -----------------------------------------------=
------------------------------------

# IMAGE TO STRING
#img =3D Image.open("temp/noBorders.jpg")
#text =3D pytesseract.image_to_string(img)
#print(text)




XXXXXXXXXXXXXXXXXXX

import pytesseract
from PIL import Image
import cv2


#img =3D Image.open('text.png')  # IMG_0001.jpg, 6822, Untitled, text.png
#text =3D pytesseract.image_to_string(img)
#print(text)

myconfig =3D r"--psm 11 --oem 3"

img =3D cv2.imread("test.jpg")
height, width, _ =3D img.shape

boxes =3D pytesseract.image_to_boxes(img, config=3Dmyconfig)
for box in boxes.splitlines():
    box =3D box.split(" ")
    img =3D cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(bo=
x[3]), height - int(box[4])), (0, 255, 0), 2)

# Display Final Image in window
cv2.namedWindow("display", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("display", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSC=
REEN)
cv2.imshow("display", img) ##
cv2.waitKey(0)
