#certain Mouse event triggers certain actions
import cv2
import numpy as np

image = cv2.imread(r'C:\Users\aksha\OneDrive\Desktop\python\Python Program\Io\Akshatha_1.png',1)

def mouse_event(event, x, y, flags, param):
    global image

    if event == cv2.EVENT_LBUTTONDOWN:  # Left click
        print(f"Left click at position: ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONDOWN:  # Right click
        radius = 5
        cv2.circle(image, (x, y), radius, (255, 0, 255), -1)  
        cv2.imshow('Image', image)
    elif event == cv2.EVENT_LBUTTONDBLCLK:  # Left double click
        cv2.circle(image, (x, y), 20, (255, 255, 255), -1)
        cv2.imshow('Image', image)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_event)
while True:
    cv2.imshow('Image', image)
    key = cv2.waitKey(0)
    if key == ord('p'):
        break
cv2.destroyAllWindows()
