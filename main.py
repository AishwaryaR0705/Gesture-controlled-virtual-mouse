import math
import cv2
import pyautogui
from hand_tracking import HandTracker

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(3, 1280)
cap.set(4, 720)
tracker = HandTracker()
screenW, screenH = pyautogui.size()

dragging = False
rightClicking = False
scrolling = False

while True:
    success, img = cap.read()
    if not success:
        print("Camera not working")
        break
    img = tracker.findHands(img)
    lmList = tracker.findPosition(img)
    
    if len(lmList) != 0:
        x1 = lmList[8][1]
        y1 = lmList[8][2]

        x2 = lmList[4][1]
        y2 = lmList[4][2]
        
        x3 = lmList[12][1]
        y3 = lmList[12][2]

        screenX = screenW / 1280 * x1
        screenY = screenH / 720 * y1

        pyautogui.moveTo(screenX, screenY)

        distance = math.hypot(x2 - x1, y2 - y1)
        distance2 = math.hypot(x2 - x3, y2 - y3)
        scrollDistance = math.hypot(x1 - x3, y1- y3)
        if distance < 40 and dragging == False:
            pyautogui.mouseDown()
            dragging =True
        if distance > 40 and dragging == True:
            pyautogui.mouseUp()
            dragging = False
        if distance2 < 40 and rightClicking == False:
            pyautogui.rightClick()
            rightClicking = True

        if distance2 > 40:
            rightClicking = False
        if scrollDistance < 40 and scrolling == False:
            pyautogui.scroll(50)
            scrolling = True
        if scrollDistance > 40:
            scrolling = False

           
    cv2.imshow("Virtual Mouse", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break