# Import required packages
import cv2
import pytesseract
 
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

from googletrans import Translator

translator = Translator()

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = 'D:\\Installs\\Tesseract-OCR\\tesseract.exe'
 
# Read image from which text needs to be extracted
img = cv2.imread("page0.png")
 
# Preprocessing the image starts
 
# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
 
# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
 
# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
 
# Finding contours
contours_1, hierarchy_2 = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)

 
# Creating a copy of image
im2 = img.copy()
 
# A text file is created and flushed
file = open("recognized.txt", "w+", encoding='utf-8')
file.write("")
file.close()
 
# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
counter = 0

for cnt in contours_1:

    x, y, w, h = cv2.boundingRect(cnt)
     
    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), -1)

for cnt in contours_1:

    x, y, w, h = cv2.boundingRect(cnt)
     
    # Drawing a rectangle on copied image
    #rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), -1)
     
    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]

    ## looking at cropped
    # cv2.namedWindow('img', 0)
    # cv2.imshow('img', cropped)
    # while(cv2.waitKey()!=ord('q')):
    #     continue
    # cv2.destroyAllWindows()

    # convert cropped to an image first
    #im = Image.fromarray(np.uint8(cm.gist_earth(cropped)*255))
    im = Image.fromarray(cropped.astype('uint8'), 'RGB')

    # enhancing image
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save(f'p{counter}.jpg')
    custom_config = r'--oem 3 --psm 9 -l ben'
    text = pytesseract.image_to_string(Image.open(f'p{counter}.jpg'), config=custom_config)

    # try:
    #     print(translator.detect(str(text)))
    # except Exception as e:
    #     print(e)

    print(text)
    if(len(text)>0):
        try: 
            text1 = str(translator.translate(str(text), src='bn', dst='en'))
        except Exception as e:
            text1 = '<redacted>'
        # Open the file in append mode
        file = open("recognized.txt", "a", encoding='utf-8')
     
        #print(text)
        # Appending the text into file

        cv2.putText(im2, text1, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

        file.write(text1)
     
         # Close the file
        file.close()

    counter += 1

cv2.namedWindow('img', 0)
cv2.namedWindow("img", cv2.WINDOW_NORMAL);
cv2.setWindowProperty ("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);
cv2.imshow('img', im2)
while(cv2.waitKey()!=ord('q')):
    continue
cv2.destroyAllWindows()