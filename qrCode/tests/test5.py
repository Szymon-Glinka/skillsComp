import cv2
import numpy as np

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



# Display the image with corners
cv2.imshow("Corners", corner_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Create a mask for the red corners
red_mask = np.zeros_like(gray)
red_mask[corners > threshold] = 255

# Apply the red mask to the image
masked_image = cv2.bitwise_and(image, image, mask=red_mask)



# Display the image with corners
cv2.imshow("Corners", masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()