import cv2
import numpy as np
import os
from cvzone.HandTrackingModule import HandDetector  # 👈 using cvzone

#######################
brushThickness = 25
eraserThickness = 100
########################

folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)

overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    image = cv2.resize(image, (1280, 125))  # 👈 Resize to match webcam width
    overlayList.append(image)

print(len(overlayList))
header = overlayList[0]
drawColor = (255, 0, 255)

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize hand detector
detector = HandDetector(detectionCon=0.65, maxHands=1)

xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    # 1. Import image
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    hands, img = detector.findHands(img, draw=True)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]  # Landmark list
        fingers = detector.fingersUp(hand)  # Which fingers are up

        x1, y1 = lmList[8][0:2]   # Index finger tip
        x2, y2 = lmList[12][0:2]  # Middle finger tip

        # 3. Selection Mode - Two fingers up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")
            if y1 < 125:  # If hand is in header area
                if 250 < x1 < 450:
                    header = overlayList[0]
                    drawColor = (255, 0, 255)
                elif 550 < x1 < 750:
                    header = overlayList[1]
                    drawColor = (255, 0, 0)
                elif 800 < x1 < 950:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                elif 1050 < x1 < 1200:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

        # 4. Drawing Mode - Only Index finger up
        elif fingers[1] and not fingers[2]:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            # Eraser
            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1

    # 5. Merge canvas and main image
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # 6. Display header
    img[0:125, 0:1280] = header

    cv2.imshow("Image", img)
    cv2.imshow("Canvas", imgCanvas)
    cv2.waitKey(1)
