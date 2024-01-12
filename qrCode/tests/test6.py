import cv2
from pyzbar import pyzbar
from PIL import Image


def basicFix(path):
    '''This function applies a Gaussian blur to the image and trys to decode the QR code.
    Takes the path of the image as input and returns the QR code data and the blurred image.'''

    #==== Apply guassian blur ====
    image = cv2.imread(path) #Load the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Convert the image to grayscale
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) #Apply Gaussian blur to reduce noise
    qr_code = pyzbar.decode(blurred) #Detect QR codes in the blurred image

    #--- If QR code is detected extract it's data---
    if len(qr_code) > 0:
        data = qr_code[0].data.decode("utf-8")
    else:
        data = None
    
    return data, blurred

def mark_qr_code(image):
    '''This function takes an image as input and marks the QR code if detected.
    returns the marked image.'''
    
    #==== Mark QR code ====
    colorOutline = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB) #Convert the image to color
    qr_code = pyzbar.decode(image) #Detect QR codes in the blurred image

    #--- If QR code is detected ---
    if qr_code:
            (x, y, w, h) = qr_code[0].rect #Extract the QR code data
            cv2.rectangle(colorOutline, (x, y), (x + w, y + h), (0, 255, 0), 2) #Draw a green rectangle around the QR code

    finalImage = Image.fromarray(colorOutline) #Convert the image to PIL format

    return finalImage

# Example usage
image_path = r"F:\skillscomp\z4codes\F.jpg"
data, image = basicFix(image_path)
print(data)
mark_qr_code(image)
