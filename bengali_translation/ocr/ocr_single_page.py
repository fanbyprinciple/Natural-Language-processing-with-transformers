import cv2
import pytesseract
import os


path = '/home/misthios/Documents/Natural-Language-processing-with-transformers/bengali_translation/ocr/inp/9.png'

# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

image = cv2.imread(f'{path}')
text = pytesseract.image_to_string(image,lang='ben')
f1 = open('single_page.txt' , 'w+', encoding='UTF-8')
f1.write(text)
f1.close()

print('OCR extracted into single_page.txt')