import cv2 as cv
import pyautogui as pt
import numpy as np
import time

costs = cv.imread('measure.png', 0)
wcost = costs.shape[0]
hcost = costs.shape[1]

while True:
    pt.screenshot('screen.png', region=(0, 0, 954, 550))
    level = cv.imread("screen.png", 0)
    portal = cv.imread('portal.png', 0)

    result = cv.matchTemplate(level, portal, cv.TM_CCOEFF_NORMED)

    min_val1, max_val1, min_loc1, max_loc1 = cv.minMaxLoc(result)
    if max_val1 < .6:
        continue
    break

level = cv.imread('screen.png', 0)
mine = cv.imread('b.png', 0)

result = cv.matchTemplate(level, mine, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

w1 = mine.shape[1]
h1 = mine.shape[0]

a = max_loc[0]-w1
b = max_loc[1]-h1

cv. rectangle(level, (a, b),
              (max_loc[0] + w1 + w1, max_loc[1] + h1 + h1), 0, -1)


def loc1(limit, xmin, xmax, ymin, ymax):
    plate = cv.imread('damage.png', 0)
    result = cv.matchTemplate(level, plate, cv.TM_CCOEFF_NORMED)

    w = plate.shape[1]
    h = plate.shape[0]

    yloc, xloc = np.where(result >= .8)

    rectangles = []

    for(x, y) in zip(xloc, yloc):
        if xmin < x < xmax and ymin < y < ymax:
            rectangles.append(
                [int(x), int(y), int(w), int(h)])

    rectangles, weights = cv.groupRectangles(
        rectangles, 1, 1)

    atack = len(rectangles)

    if atack != 0:
        for(x, y, w, h) in rectangles:
            cv.rectangle(level, (x, y), (x + w, y + h), (0, 255, 255), 1)
        print(len(rectangles))

    elif atack == 0:
        print('none atack plates!!!')

    plate = cv.imread('reload.png', 0)
    result = cv.matchTemplate(level, plate, cv.TM_CCOEFF_NORMED)

    w = plate.shape[1]
    h = plate.shape[0]

    yloc, xloc = np.where(result >= .7)

    rectangles = []

    for(x, y) in zip(xloc, yloc):
        if xmin < x < xmax and ymin < y < ymax:
            rectangles.append(
                [int(x), int(y), int(w), int(h)])

    rectangles, weights = cv.groupRectangles(
        rectangles, 1, 1)

    rel = len(rectangles)
    positive = limit-atack

    if rel != 0:
        for(x, y, w, h) in rectangles[:positive]:
            cv.rectangle(level, (x, y), (x + w, y + h), (0, 255, 255), 1)
        print(len(rectangles))

    elif rel == 0:
        print('none reload plates!!!')

    elif positive < 0:
        print('positive is negative')

    plate = cv.imread('exp.png', 0)
    result = cv.matchTemplate(level, plate, cv.TM_CCOEFF_NORMED)

    w = plate.shape[1]
    h = plate.shape[0]

    yloc, xloc = np.where(result >= .7)

    rectangles = []

    for(x, y) in zip(xloc, yloc):
        if xmin < x < xmax and ymin < y < ymax:
            rectangles.append(
                [int(x), int(y), int(w), int(h)])

    rectangles, weights = cv.groupRectangles(
        rectangles, 1, 1)

    exp = len(rectangles)
    positive = limit-atack-rel

    if exp != 0:
        for(x, y, w, h) in rectangles[:positive]:
            cv.rectangle(level, (x, y), (x + w, y + h), (0, 255, 255), 1)
        print(len(rectangles))

    elif exp == 0:
        print('none exp plates!!!')

    elif positive < 0:
        print('positive is negative')

    plate = cv.imread('radius.png', 0)
    result = cv.matchTemplate(level, plate, cv.TM_CCOEFF_NORMED)

    w = plate.shape[1]
    h = plate.shape[0]

    yloc, xloc = np.where(result >= .7)

    rectangles = []

    for(x, y) in zip(xloc, yloc):
        if xmin < x < xmax and ymin < y < ymax:
            rectangles.append(
                [int(x), int(y), int(w), int(h)])

    rectangles, weights = cv.groupRectangles(
        rectangles, 1, 1)

    rad = len(rectangles)
    positive = limit-atack-rel-exp

    if rad != 0 and positive > 0:
        for(x, y, w, h) in rectangles[:positive]:
            cv.rectangle(level, (x, y), (x + w, y + h), (0, 255, 255), 1)
        print(len(rectangles))

    elif rad == 0:
        print('none radius plates!!!')

    elif positive < 0:
        print('positive is negative')

    plate = cv.imread('plate.png', 0)
    result = cv.matchTemplate(level, plate, cv.TM_CCOEFF_NORMED)

    w = plate.shape[1]
    h = plate.shape[0]

    yloc, xloc = np.where(result >= .8)

    rectangles = []

    for(x, y) in zip(xloc, yloc):
        if xmin < x < xmax and ymin < y < ymax:
            rectangles.append(
                [int(x), int(y), int(w), int(h)])

    rectangles, weights = cv.groupRectangles(
        rectangles, 1, 1)

    plate = len(rectangles)
    positive = limit-rad-atack-rel-exp

    if plate != 0 and positive > 0:
        for(x, y, w, h) in rectangles[:positive]:
            cv.rectangle(level, (x, y), (x + w, y + h), (0, 255, 255), 1)
        print(len(rectangles))

    elif plate == 0:
        print('none plate!!!')

    elif positive < 0:
        print('positive is negative')

    cv.imshow('rr', level)
    cv.waitKey()
    cv.destroyAllWindows()


loc1(5, max_loc1[0]-wcost*4, max_loc1[0]+wcost*4, max_loc1[1]-hcost*4, max_loc1[1]+hcost*4)
