from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def pavlidis_outer_contour(binary_array):
    def move_forward(position, direction):
        return (position[0] + direction[0], position[1] + direction[1])

    def is_black(pixel, binary_array):
        x, y = pixel
        return 0 <= x < binary_array.shape[0] and 0 <= y < binary_array.shape[1] and binary_array[x, y] == 0

    def has_black_neighbor(pixel, binary_array):
        x, y = pixel
        neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1),
                     (x, y-1),             (x, y+1),
                     (x+1, y-1), (x+1, y), (x+1, y+1)]
        return any(0 <= nx < binary_array.shape[0] and 0 <= ny < binary_array.shape[1] and binary_array[nx, ny] == 0 for nx, ny in neighbors)

    # Find all black pixels
    black_pixels = [(i, j) for i in range(binary_array.shape[0]) for j in range(binary_array.shape[1]) if is_black((i, j), binary_array)]

    # Filter out black pixels that have black neighbors on all sides and diagonals
    outer_contour = [pixel for pixel in black_pixels if has_black_neighbor(pixel, binary_array)]

    # Sort the contour points to trace from bottom left to top left to top right to bottom right
    outer_contour.sort(key=lambda p: (p[1], -p[0]))

    return outer_contour

# Load the image
image_path = "bubrek.jpg"
image = Image.open(image_path).convert("L")  # Convert to grayscale

# Threshold the image to create a binary representation (black and white)
threshold = 128
binary_image = image.point(lambda p: p < threshold and 255)

# Apply Pavlidis' algorithm to find the outer contour
outer_contour_sequence = pavlidis_outer_contour(np.array(binary_image) == 0)  # Use True for black pixels

# Plotting the original image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

# Plotting the found outer contour
plt.subplot(1, 2, 2)
plt.imshow(image, cmap='gray')

# Extracting x and y coordinates
outer_contour_x, outer_contour_y = zip(*outer_contour_sequence)

# Plotting the outer contour using plt.plot
plt.plot(outer_contour_y + (outer_contour_y[0],), outer_contour_x + (outer_contour_x[0],), color='red', linewidth=2)

# Setting the aspect ratio to match the image
plt.gca().set_aspect('equal', adjustable='box')

plt.title("Outer Contour")

plt.show()
