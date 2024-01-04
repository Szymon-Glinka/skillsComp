import cv2
from pyzbar import pyzbar

def read_blurred_qr_code(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect QR codes in the blurred image
    qr_codes = pyzbar.decode(blurred)

    # Extract and print the QR code data
    for qr_code in qr_codes:
        data = qr_code.data.decode("utf-8")
        print("QR Code Data:", data)

    #show
    cv2.imshow("blurred", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
#Back
image_path = r"F:\skillscomp\z4codes\FB.jpg"
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

