import numpy as np
import cv2


def detectColor(path):
    hsvCodes = {
        "red": [(0, 70, 10), (19, 255, 255), (0, 0, 255)],
        "green": [(52, 90, 0), (155, 255, 255), (0, 255, 0)],
        "blue": [(160, 90, 10), (260, 255, 255), (255, 0, 0)],
        "yellow": [(26, 90, 10), (45, 255, 255), (0, 255, 255)],
    }

    image = cv2.imread(path)
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    black_backgroundF = np.zeros_like(image)

    for color, (lowerLimit, upperLimit, outlineColor) in hsvCodes.items():
        lowerLimit = np.array(lowerLimit)
        upperLimit = np.array(upperLimit)
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        result = cv2.bitwise_and(hsvImage, image, mask=mask)

        # Convert the result to black and white
        result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        _, result_bw = cv2.threshold(result_gray, 1, 255, cv2.THRESH_BINARY)

        # Create a black background
        black_background = np.zeros_like(image)
        


        # Show the result
        contours, _ = cv2.findContours(result_bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(black_background, contours, -1, outlineColor, 2)

        # Append the outline to the final image
        black_backgroundF = cv2.add(black_backgroundF, black_background)

    cv2.imshow("Final Image", black_backgroundF)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

        

        

    



path = r'F:\skillscomp\z3colors\YR.jpg'
detectColor(path)