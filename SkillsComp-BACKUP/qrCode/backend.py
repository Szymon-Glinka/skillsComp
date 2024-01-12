import cv2
from pyzbar import pyzbar
import numpy as np
from PIL import Image


def basicFix(image):
    '''This function applies a Gaussian blur to the image and trys to decode the QR code.
    Takes the image as input and returns the QR code data and the blurred image.'''

    #==== Apply guassian blur ====
    blurred = cv2.GaussianBlur(image, (5, 5), 0) #Apply Gaussian blur to reduce noise
    qr_code = pyzbar.decode(blurred) #Detect QR codes in the blurred image

    #--- If QR code is detected extract it's data---
    if len(qr_code) > 0:
        data = qr_code[0].data.decode("utf-8")
    else:
        data = None
    
    return data, blurred


def fixBlur(image):
    '''This function applies a detail enhancement filter to the image and trys to decode the QR code.
    Takes thethe image as input and returns the QR code data and the enhanced image.'''

    #==== set variables ====
    repeat = True
    listOfSimgaS = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200]
    listOfSigmaR = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1]
    sS = 0
    sR = 0

    #==== Fixing blur ====
    while repeat:
        enhanced_image = cv2.detailEnhance(image, sigma_s=listOfSimgaS[sS], sigma_r=listOfSigmaR[sR]) #Enhance the image
        qr_code = pyzbar.decode(enhanced_image) #try to decode qr code

        #--- If QR code is detected ---
        if len(qr_code) > 0:
            repeat = False #stop the loop
            data = qr_code[0].data.decode("utf-8") #Extract the QR code data
            return data, enhanced_image
    
        #--- If QR code is not detected ---
        sR += 1 #increase sigmaR
        if sR >= len(listOfSigmaR): #if sigmaR is out of range
            sS += 1 #increase sigmaS
            sR = 0 #reset sigmaR

        #--- If sigmaS and sigmaR are out of range return none bc no QR code detected---
        if sS >= len(listOfSimgaS)-1 and sR >= len(listOfSigmaR)-1:
            repeat = False #stop the loop
            return None, image
        

def fixPos(image):
    '''This function applies a perspective transformation to the image and trys to decode the QR code.
    Takes the path of the image as input and returns the QR code data and the transformed image.''' 

    #==== Basic post-processing ====
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Convert the image to grayscale

    #==== Corner detection ====
    corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04) #Detect corners using the Harris corner detection algorithm

    #--- Threshold the corner response to obtain the corners ---
    threshold = 0.001 * corners.max()
    corner_image = image.copy()
    corner_image[corners > threshold] = [0, 0, 255]  #Mark corners in red

    corner_coords = np.argwhere(corners > threshold) #Find the coordinates of the corners

    #--- Finds the coordinates of the points closest to each corner [y, x]---
    top_left = corner_coords[np.argmin(corner_coords[:, 0] + corner_coords[:, 1])]
    top_right = corner_coords[np.argmin(corner_coords[:, 0] - corner_coords[:, 1])]
    bottom_left = corner_coords[np.argmin(-corner_coords[:, 0] + corner_coords[:, 1])]
    bottom_right = corner_coords[np.argmin(-corner_coords[:, 0] - corner_coords[:, 1])]

    #==== Perspective transformation ====
    input_pts = np.float32([[top_left[1], top_left[0]],[bottom_left[1], bottom_left[0]],[bottom_right[1], bottom_right[0]],[top_right[1], top_right[0]]]) #set coordinates of the detrected corners of the QR code

    height, _, _ = image.shape #get the height of the image
    dimQr = height/2 #set the dimension of the fixed QR code

    #--- Set the coordinates of the corners of the fixed QR code ---
    topLeft = [0, 0]
    bottomLeft = [0, dimQr]
    bottomRight = [dimQr, dimQr]
    topRight = [dimQr, 0]
    output_pts = np.float32([topLeft, bottomLeft, bottomRight, topRight])

    M = cv2.getPerspectiveTransform(input_pts,output_pts) #get the transformation matrix
    fixedQRcode = cv2.warpPerspective(image,M,(image.shape[1], image.shape[0]),flags=cv2.INTER_LINEAR) #apply the transformation matrix

    #==== QR code detection ====
    qr_code = pyzbar.decode(fixedQRcode) #Detect QR codes in the blurred image
    
    #--- If QR code is detected extract it's data---
    if len(qr_code) > 0:
        data = qr_code[0].data.decode("utf-8")
    else:
        data = None

    return data, fixedQRcode


def markQRcode(image):
    '''This function takes an image as input and marks the QR code if detected.
    returns the marked image.'''
    
    #==== Mark QR code ====
    colorOutline = image #Convert the image to color
    qr_code = pyzbar.decode(image) #Detect QR codes in the blurred image

    #--- If QR code is detected ---
    if qr_code:
            (x, y, w, h) = qr_code[0].rect #Extract the QR code data
            cv2.rectangle(colorOutline, (x, y), (x + w, y + h), (0, 255, 0), 4) #Draw a green rectangle around the QR code

    finalImage = Image.fromarray(colorOutline) #Convert the image to PIL format

    return finalImage