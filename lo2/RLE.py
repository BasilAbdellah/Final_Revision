import cv2
import numpy as np


def RLE(image):
    count = 1
    # Flatten the image into a 1D array for processing
    flat_image = image.flatten()

    # Set the first element as the starting value
    prev_char = flat_image[0]  # Now this is a scalar value
    new_list = []

    for char in flat_image[1:]:
        if char == prev_char:
            count += 1
        else:
            new_list.append((count, prev_char))
            prev_char = char
            count = 1

    # Append the last (count, value) pair
    new_list.append((count, prev_char))
    return new_list


# Read the image in grayscale mode
image = cv2.imread("sea.bmp", cv2.IMREAD_GRAYSCALE)

# Apply RLE
edit = RLE(image)

# Save and display the images
cv2.imwrite("edited.bmp", image)
cv2.imshow('original', image)
cv2.imshow('edited', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
