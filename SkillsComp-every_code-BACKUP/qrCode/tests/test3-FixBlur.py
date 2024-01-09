import cv2
from pyzbar import pyzbar

repeat = True
listOfSimgaS = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200]
listOfSigmaR = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1]
sS = 0
sR = 0

# Load the image
image = cv2.imread(r"F:\skillscomp\z4codes\L.jpg")


while repeat:
    enhanced_image = cv2.detailEnhance(image, sigma_s=listOfSimgaS[sS], sigma_r=listOfSigmaR[sR])
    qr_codes = pyzbar.decode(enhanced_image)

    if len(qr_codes) > 0:
        repeat = False
        for qr_code in qr_codes:
            data = qr_code.data.decode("utf-8")
            print("QR Code Data:", data)
    
    sR += 1
    if sR >= len(listOfSigmaR):
        sS += 1
        sR = 0
