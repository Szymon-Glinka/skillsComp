import cv2
from pyzbar import pyzbar
import numpy as np

def read_blurred_qr_code(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    sharpened = cv2.GaussianBlur(image, (0, 0), 3)
    sharpened = cv2.addWeighted(image, 1.5, sharpened, -0.5, 0)


    # Detect QR codes in the blurred image
    qr_codes = pyzbar.decode(sharpened)

    # Extract and print the QR code data
    for qr_code in qr_codes:
        data = qr_code.data.decode("utf-8")
        print("QR Code Data:", data)

    #show
    cv2.imshow('Sharpened', sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
#Back
image_path = r"F:\skillscomp\z4codes\B.jpg"
print("B: ")
read_blurred_qr_code(image_path)
#Forward
image_path = r"F:\skillscomp\z4codes\F.jpg"
print("F: ")
read_blurred_qr_code(image_path)
#Left
image_path = r"F:\skillscomp\z4codes\L.jpg"
print("L: ")
read_blurred_qr_code(image_path)
#Right
image_path = r"F:\skillscomp\z4codes\R.jpg"
print("R: ")
read_blurred_qr_code(image_path)