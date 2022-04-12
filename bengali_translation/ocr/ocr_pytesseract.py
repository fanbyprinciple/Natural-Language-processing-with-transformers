import cv2
import pytesseract
import os
from sys import argv

path = './'
dirs = os.listdir(path)

print(dirs)

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

for i in dirs:
    image = cv2.imread(f'{path}/pages/{i}')
    #ocr\pages\page0.png
    text = pytesseract.image_to_string(image,lang='ben')
    print('Writing to ' + i )

    f1 = open('{path}/result/result' + i + '.txt', 'w+', encoding='UTF-8')

    f1.write(text)
    f1.close()

# cv2.imshow('Image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()