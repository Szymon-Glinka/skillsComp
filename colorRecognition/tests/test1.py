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

path = r'F:\skillscomp\z3colors\YGR3.png'
colors, image, dim = detectColor_markOutlines(path)
print(colors, dim)
image.show()