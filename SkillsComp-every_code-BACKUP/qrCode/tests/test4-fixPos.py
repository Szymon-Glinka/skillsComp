import cv2
import numpy as np
from pyzbar import pyzbar

# Load the image
image = cv2.imread(r"F:\skillscomp\z4codes\B.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect corners using the Harris corner detection algorithm
corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Threshold the corner response to obtain the corners
threshold = 0.001 * corners.max()
corner_image = image.copy()
corner_image[corners > threshold] = [0, 0, 255]  # Mark corners in red

# Find the coordinates of the corners
corner_coords = np.argwhere(corners > threshold)

# Find the points closest to each corner [y, x]
top_left = corner_coords[np.argmin(corner_coords[:, 0] + corner_coords[:, 1])]
top_right = corner_coords[np.argmin(corner_coords[:, 0] - corner_coords[:, 1])]
bottom_left = corner_coords[np.argmin(-corner_coords[:, 0] + corner_coords[:, 1])]
bottom_right = corner_coords[np.argmin(-corner_coords[:, 0] - corner_coords[:, 1])]

# Print the coordinates of the points closest to each corner
print("Top Left:", top_left)
print("Top Right:", top_right)
print("Bottom Left:", bottom_left)
print("Bottom Right:", bottom_right)


# to calculate the transformation matrix
input_pts = np.float32([[top_left[1], top_left[0]],[bottom_left[1], bottom_left[0]],[bottom_right[1], bottom_right[0]],[top_right[1], top_right[0]]])


height, width, _ = image.shape
dimQr = height/2

topLeft = [0, 0]
bottomLeft = [0, dimQr]
bottomRight = [dimQr, dimQr]
topRight = [dimQr, 0]



output_pts = np.float32([topLeft, bottomLeft, bottomRight, topRight])



# Compute the perspective transform M
M = cv2.getPerspectiveTransform(input_pts,output_pts)
 
# Apply the perspective transformation to the image

out = cv2.warpPerspective(image,M,(image.shape[1], image.shape[0]),flags=cv2.INTER_LINEAR)
 
# Display the transformed image
cv2.imshow("aaa", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detect QR codes in the blurred image
qr_codes = pyzbar.decode(out)

# Extract and print the QR code data
for qr_code in qr_codes:
    data = qr_code.data.decode("utf-8")
    print("QR Code Data:", data)
