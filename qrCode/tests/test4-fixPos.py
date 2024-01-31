import cv2
import numpy as np
from pyzbar import pyzbar

def fixPos(path):
    '''This function applies a perspective transformation to the image and trys to decode the QR code.
    Takes the path of the image as input and returns the QR code data and the transformed image.''' 

    #==== Basic post-processing ====
    image = cv2.imread(path) #Load the image
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

if __name__ == "__main__":
    path = r"F:\skillscomp\z4codes\B.jpg"
    fixPos(path)