import cv2
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
pytesseract.pytesseract.tesseract_cmd = r'D:\\Installs\\Tesseract-OCR\\'


img = cv2.imread('page2.png')
mser = cv2.MSER_create()

#Resize the image so that MSER can work better
img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()

i2b = pytesseract.image_to_boxes(gray)

#print(i2b)
still = []
bboxes = []
for i in i2b.split():

    if (i.isdigit()):
        still.append(int(i))
    else:
        bboxes.append(still)
        still = []

bboxes = bboxes[1:]
#print(bboxes)

print(type(i2b))
#coordinates, bboxes = mser.detectRegions(gray)
for bbox in bboxes:
    index_arr = bbox
    cv2.rectangle(vis, (index_arr[0]-15, index_arr[1]-15), (index_arr[0] + index_arr[2] + 15, index_arr[1] + index_arr[3] + 15), (120,120,120), 2)

for bbox in bboxes:
    index_arr = bbox
    cv2.putText(vis, 'O', (index_arr[0], index_arr[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

cv2.namedWindow('img', 0)
cv2.namedWindow("img", cv2.WINDOW_NORMAL);
cv2.setWindowProperty ("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);
cv2.imshow('img', vis)
while(cv2.waitKey()!=ord('q')):
    continue
cv2.destroyAllWindows()