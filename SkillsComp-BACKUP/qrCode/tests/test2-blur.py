import cv2
from pyzbar import pyzbar

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
    

if __name__ == "__main__":
    image_path = r"F:\skillscomp\z4codes\R.jpg"
    data, _ = basicFix(image_path)
    print(data)
