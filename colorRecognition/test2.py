import cv2
import numpy as np

# Load the image
image = cv2.imread(r'F:\skillscomp\z3colors\YR.jpg')

hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the color range to be outlined (in BGR format)
lower_color = (0, 70, 10)  # Lower threshold for the color
upper_color = (19, 255, 255)  # Upper threshold for the color

# Create a mask for the specified color range
mask = cv2.inRange(hsvImage, lower_color, upper_color)

# Apply the mask to the image
result = cv2.bitwise_and(hsvImage, image, mask=mask)

# Convert the result to black and white
result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
_, result_bw = cv2.threshold(result_gray, 1, 255, cv2.THRESH_BINARY)

# Create a black background
black_background = np.zeros_like(image)

# Show the result
contours, _ = cv2.findContours(result_bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(black_background, contours, -1, (0, 0, 255), 2)

cv2.imshow('Result', black_background)
cv2.waitKey(0)
cv2.destroyAllWindows()

