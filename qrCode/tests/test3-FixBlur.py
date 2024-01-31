import cv2
from pyzbar import pyzbar


def fixBlur(path):
    '''This function applies a detail enhancement filter to the image and trys to decode the QR code.
    Takes the path of the image as input and returns the QR code data and the enhanced image.'''

    #==== set variables ====
    repeat = True
    listOfSimgaS = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200]
    listOfSigmaR = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1]
    sS = 0
    sR = 0

    #==== Fixing blur ====
    image = cv2.imread(path) #Load the image

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
        if sS >= len(listOfSimgaS) and sR >= len(listOfSigmaR):
            repeat = False #stop the loop
            return None, image

if __name__ == "__main__":
    path = r"F:\skillscomp\z4codes\L.jpg"
    fixBlur(path)