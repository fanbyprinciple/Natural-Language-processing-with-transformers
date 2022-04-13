import cv2

img = cv2.imread('page0.png')
mser = cv2.MSER_create()

#Resize the image so that MSER can work better
img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()

## bounding box logic

# regions = mser.detectRegions(gray)
# #print('regions', regions)
# hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
# print('hulls',hulls)

# for i in hulls:
#     print (i)
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#     input()
# cv2.polylines(vis, hulls, 1, (0,255,0),2) 

#https://stackoverflow.com/questions/48615935/merging-regions-in-mser-for-identifying-text-lines-in-ocr
coordinates, bboxes = mser.detectRegions(gray)
for bbox in bboxes:
    x, y, w, h = bbox
    cv2.rectangle(vis, (x-15, y-15), (x + w + 15, y + h+ 15), (255,255,255), -1)
    cv2.putText(vis, 'F', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

cv2.namedWindow('img', 0)
cv2.namedWindow("img", cv2.WINDOW_NORMAL);
cv2.setWindowProperty ("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);
cv2.imshow('img', vis)
while(cv2.waitKey()!=ord('q')):
    continue
cv2.destroyAllWindows()