import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

def recognize_colors(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the colors you want to recognize
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([70, 255, 255])
    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])

    # Create masks for each color range
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Apply the masks to the original image
    red_result = cv2.bitwise_and(image, image, mask=red_mask)
    green_result = cv2.bitwise_and(image, image, mask=green_mask)
    blue_result = cv2.bitwise_and(image, image, mask=blue_mask)

    # Display the results
    cv2.imshow("Red", red_result)
    cv2.imshow("Green", green_result)
    cv2.imshow("Blue", blue_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = r"C:\Users\MSI\Desktop\robotyka\YGR2.png"
recognize_colors(image_path)
    
# Create a tkinter window
window = tk.Tk()

# Create a button to upload an image
upload_button = tk.Button(window, text="Upload Image", command=recognize_colors)
upload_button.pack()

# Start the tkinter event loop
window.mainloop()
