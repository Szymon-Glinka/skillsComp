import numpy as np
import cv2
from PIL import Image

def detectColor_markOutlines(path):
    """This function takes path to image as input and returns the list of colors found and the final image with the outlines and dimensions of the image.
    This function marks the exact outlines of the objects of each color in that color on a black background.
    Disclaimer: this function only works for the colors red, green, blue and yellow. And its not perfect for those colors either. To add more colors you need to add their HSV color ranges to the hsvCodes dictionary."""

    hsvCodes = { # HSV color ranges for the R, G, B, Y colors
        "red": [(0, 70, 10), (19, 255, 255), (0, 0, 255)],
        "green": [(52, 90, 0), (155, 255, 255), (0, 255, 0)],
        "blue": [(160, 90, 10), (260, 255, 255), (255, 0, 0)],
        "yellow": [(26, 90, 10), (45, 255, 255), (0, 255, 255)],
    }
    foundColors = [] # List of colors found in the image

    #--- Read the image and convert it to HSV and create background for final image and get width and height---
    image = cv2.imread(path)
    imageHeight, imageWidth, imageChannels = image.shape
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    outlinesArray = np.zeros_like(image) #create background for final image - all the countours

    #--- Loop through the colors ---
    for color, (lowerLimit, upperLimit, outlineColor) in hsvCodes.items(): 
        #--- Create a mask for the color ---
        lowerLimit = np.array(lowerLimit) #convert lowerLimit to numpy array
        upperLimit = np.array(upperLimit) #convert upperLimit to numpy array
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) #create mask
        result = cv2.bitwise_and(hsvImage, image, mask=mask) #apply mask to image

        #--- Count the number of non-black pixels in the mask and append the color to the list ---
        count = cv2.countNonZero(mask)
        if count > 0:
            foundColors.append(color)

        #--- Convert the result to black and white and create black background ---
        result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        _, result_bw = cv2.threshold(result_gray, 1, 255, cv2.THRESH_BINARY)
        black_background = np.zeros_like(image) #create background for each color

        #--- Find the contours and draw them on the black background ---
        contours, _ = cv2.findContours(result_bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(black_background, contours, -1, outlineColor, 2)

        #--- Add the contours to the final image ---
        outlinesArray = cv2.add(outlinesArray, black_background)

    #--- Convert the final image to PIL image ---
    color_coverted = cv2.cvtColor(outlinesArray, cv2.COLOR_BGR2RGB) #convert to RGB
    finalOutlines = Image.fromarray(color_coverted) 
    
    return foundColors, finalOutlines, (imageHeight, imageWidth)


def detectPositionsOfColors(path):
    """This function takes path to image as input and returns the dictionary with all the info and the image with the outlines and markers and dimensions of the image.
    This function makes rectangular outlines around the objects of each color and draws a marker in the center of each object,
    additionaly it returns a dictionary of detected colors and their info (position of the marker; is it on the left, right or center; marker's offset from center of the image).
    detectedInfo = {"color": (centerX, centerY, positionX, positionY, XoffsetCenter, YoffsetCenter)}
    Disclaimer: this function only works for the colors red, green, blue and yellow. And its not perfect for those colors either. To add more colors you need to add their HSV color ranges to the hsvCodes dictionary."""

    hsvCodes = { # HSV color ranges for the R, G, B, Y colors
        "red": [(0, 70, 10), (19, 255, 255), (0, 0, 255)],
        "green": [(52, 90, 0), (155, 255, 255), (0, 255, 0)],
        "blue": [(160, 90, 10), (260, 255, 255), (255, 0, 0)],
        "yellow": [(26, 90, 10), (45, 255, 255), (0, 255, 255)],
    }
    detectedInfo = {} # Dictionary of detected colors and their info

    #--- Read the image, convert it to HSV, read dimensions of the image---
    detectedRect = cv2.imread(path)
    imageHeight, imageWidth, imageChannels = detectedRect.shape
    hsv_image = cv2.cvtColor(detectedRect, cv2.COLOR_BGR2HSV)

    #--- Loop through the colors ---
    for color, (lower, upper, marker_color) in hsvCodes.items():
        #--- reset variables ---
        position = ""
        XoffsetCenter = 0
        YoffsetCenter = 0

        #--- Create a mask for the color ---
        lower = np.array(lower, dtype=np.uint8) #convert lowerLimit to numpy array
        upper = np.array(upper, dtype=np.uint8) #convert upperLimit to numpy array
        mask = cv2.inRange(hsv_image, lower, upper) #create mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #find contours

        #--- Loop through the contours ---
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour) #get the coordinates of the contour

            #--- Calculate the center of the contour ---
            centerX = x + w//2
            centerY = y + h//2

            #--- Calculate the offset from center of image -> X---
            if centerX < (imageWidth//2):
                positionX = "left"
                XoffsetCenter = centerX - (imageWidth//2)
            elif centerX > (imageWidth//2):
                positionX = "right"
                XoffsetCenter = centerX - (imageWidth//2)
            else:
                positionX = "center"
                XoffsetCenter = 0
            
            #--- Calculate the offset from center of image -> Y---
            if centerY < (imageHeight//2):
                positionY = "top"
                YoffsetCenter = (imageHeight//2) - centerY
            elif centerY > (imageHeight//2):
                positionY = "bottom"
                YoffsetCenter = (imageHeight//2) - centerY
            else:
                positionY = "center"
                YoffsetCenter = 0

            #--- Draw the rectangle and the marker ---
            if w > 5 and h > 5:
                cv2.rectangle(detectedRect, (x, y), (x + w, y + h), marker_color, 2) #draw rectangle
                cv2.circle(detectedRect, (centerX, centerY), 5, marker_color, -1) #draw marker
                cv2.circle(detectedRect, (centerX, centerY), 6, (0, 0, 0), 1) #draw marker outline

            #--- Add the info to the dictionary ---
            detectedInfo[color] = (centerX, centerY, positionX, positionY, XoffsetCenter, YoffsetCenter) 

    #--- Convert the final image to PIL image ---
    color_coverted = cv2.cvtColor(detectedRect, cv2.COLOR_BGR2RGB) #convert to RGB
    finalRect = Image.fromarray(color_coverted) 
        
    return detectedInfo, finalRect, (imageHeight, imageWidth)