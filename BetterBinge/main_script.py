import cv2 
import numpy as np
import pyautogui
import time

template0 = cv2.imread('template0.png', 0)
template1 = cv2.imread('template1.png', 0)
template2 = cv2.imread('template2.png', 0)
template3 = cv2.imread('template3.png', 0)
template4 = cv2.imread('template4.png', 0)
template5 = cv2.imread('template5.png', 0)
template6 = cv2.imread('template6.png', 0)
nextup = cv2.imread('nextup.png', 0)



threshold = 0.8

pyautogui.alert(text='Keep the mouse pointer on the top left corner of screen to stop the program',
                title='Stopping Criteria')

while True:
    time.sleep(1)
    im1 = pyautogui.screenshot()
    im1 = np.asarray(im1.convert(mode='L'))

    for i in [template0, template1, template2, template3, template4, template5, template6]:

        res = cv2.matchTemplate(im1, i, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        # print(loc)
        w, h = i.shape[:: -1]
        if loc[0].size != 0:
            for pt in zip(*loc[:: -1]):

                x = pt[0]
                y = pt[1]
                center_x = (x + 0.5 * w)
                center_y = (y + 0.5 * h)

                pyautogui.click(center_x, center_y)

                break
            time.sleep(1)
            break

    res = cv2.matchTemplate(im1, nextup, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    # print(loc)
    w, h = i.shape[:: -1]
    if loc[0].size != 0:
        for pt in zip(*loc[:: -1]):

            x = pt[0]
            y = pt[1]
            center_x = (x + 1 * w)
            center_y = (y + 7 * h)

            pyautogui.click(center_x, center_y)
            break

    if pyautogui.position() == (0, 0):
        pyautogui.alert(text='Closed', title='BetterBinge Closed')
        break
