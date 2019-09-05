from imutils.object_detection import non_max_suppression
import numpy as np
import pytesseract
import argparse
import cv2
from prepro import process_image_for_ocr
import glob
from PIL import Image



def decode_predictions(scores, geometry):
	(numRows, numCols) = scores.shape[2:4]
	rects = []
	confidences = []


	for y in range(0, numRows):
		scoresData = scores[0, 0, y]
		xData0 = geometry[0, 0, y]
		xData1 = geometry[0, 1, y]
		xData2 = geometry[0, 2, y]
		xData3 = geometry[0, 3, y]
		anglesData = geometry[0, 4, y]

		for x in range(0, numCols):
			if scoresData[x] < args["min_confidence"]:
				continue

			(offsetX, offsetY) = (x * 4.0, y * 4.0)
			angle = anglesData[x]
			cos = np.cos(angle)
			sin = np.sin(angle)
			h = xData0[x] + xData2[x]
			w = xData1[x] + xData3[x]
			endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
			endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
			startX = int(endX - w)
			startY = int(endY - h)
			rects.append((startX, startY, endX, endY))
			confidences.append(scoresData[x])
	return (rects, confidences)


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
	help="path to input image")
ap.add_argument("-east", "--east", type=str,
	help="path to input EAST text detector")
ap.add_argument("-c", "--min-confidence", type=float, default=0.5,
	help="minimum probability required to inspect a region")
ap.add_argument("-w", "--width", type=int, default=320,
	help="nearest multiple of 32 for resized width")
ap.add_argument("-e", "--height", type=int, default=320,
	help="nearest multiple of 32 for resized height")
ap.add_argument("-p", "--padding", type=float, default=0.0,
	help="amount of padding to add to each border of ROI")
args = vars(ap.parse_args())




image = cv2.imread('page_.jpg')
image = process_image_for_ocr(image)
image = cv2.imwrite('smoo.png',image)
image = cv2.imread('smoo.png')
orig = image.copy()
(origH, origW) = image.shape[:2]


(newW, newH) = (args["width"], args["height"])
rW = origW / float(newW)
rH = origH / float(newH)

image = cv2.resize(image, (newW, newH))
(H, W) = image.shape[:2]

layerNames = [
	"feature_fusion/Conv_7/Sigmoid",
	"feature_fusion/concat_3"]

print("loading EAST text detector...")
net = cv2.dnn.readNet(args["east"])

blob = cv2.dnn.blobFromImage(image, 1.0, (W, H),
	(123.68, 116.78, 103.94), swapRB=True, crop=False)
net.setInput(blob)
(scores, geometry) = net.forward(layerNames)

(rects, confidences) = decode_predictions(scores, geometry)
boxes = non_max_suppression(np.array(rects), probs=confidences)

results = []

for (startX, startY, endX, endY) in boxes:
	startX = int(startX * rW)
	startY = int(startY * rH)
	endX = int(endX * rW)
	endY = int(endY * rH)
	dX = int((endX - startX) * args["padding"])
	dY = int((endY - startY) * args["padding"])
	startX = max(0, startX - dX)
	startY = max(0, startY - dY)
	endX = min(origW, endX + (dX * 2))
	endY = min(origH, endY + (dY * 2))
	roi = orig[startY:endY, startX:endX]
	config = ("-l swe --oem 1 --psm 7")
	text = pytesseract.image_to_string(roi, config=config)
	results.append(((startX, startY, endX, endY), text))
results = sorted(results, key=lambda r:r[0][1])
s =0
for ((startX, startY, endX, endY), text) in results:
	s=s+1
	print("{}\n".format(text))
	text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
	output = orig.copy()
	cv2.rectangle(output, (startX, startY), (endX, endY),
		(0, 0, 255), 2)
	cv2.putText(output, text, (startX, startY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
	roi = output[startY: endY	, startX: endX]
	cv2.imwrite('out/jrj'+str(s)+'.jpg',roi)

	# show the output image
	#cv2.imshow("Text Detection", output)

	#cv2.waitKey(0)

cv_img = []
for img in glob.glob("out/*.jpg"):
    n= cv2.imread(img)
    cv_img.append(n)
r = 0
for img in cv_img:
	r = r+1
	img = cv2.imwrite('lol.png',img)
	filename = 'lol.png'
	#print(img)
	textx = str(((pytesseract.image_to_string(Image.open(filename),lang="swe"))))
	# np.savetxt('Output'+str(r)+'.txt',textx, fmt='%s')
	print(textx)
	with open('textout/Output'+str(r)+'.txt', "w") as text_file:
		print(textx, file=text_file)
