import cv2
import numpy as np

# Load the blurred image
image = cv2.imread(r"F:\skillscomp\z4codes\L.jpg")


sharpen_filter=np.array([[-1,-1,-1],
                 [-1,9,-1],
                [-1,-1,-1]])
# applying kernels to the input image to get the sharpened image

sharp_image=cv2.filter2D(image,-1,sharpen_filter)



# Display the sharpened image
cv2.imshow('Sharpened Image', sharp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


