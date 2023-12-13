from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def ladybug_contour(binary_array):
    
    def is_black(pixel, binary_array):
        x, y = pixel
        return 0 <= x < binary_array.shape[0] and 0 <= y < binary_array.shape[1] and binary_array[x, y] == 0

    def is_contour(pixel, binary_array, threshold=8):
        x, y = pixel
        neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1),
                     (x, y-1),             (x, y+1),
                     (x+1, y-1), (x+1, y), (x+1, y+1)]
        return sum(1 for nx, ny in neighbors if 0 <= nx < binary_array.shape[0] and 0 <= ny < binary_array.shape[1] and binary_array[nx, ny] == 0) >= threshold

    black_pixels = [(i, j) for i in range(binary_array.shape[0]) for j in range(binary_array.shape[1]) if is_black((i, j), binary_array)]
    outer_contour = [pixel for pixel in black_pixels if not is_contour(pixel, binary_array)]

    return outer_contour

image_path = "bubrek.jpg"
image = Image.open(image_path).convert("L")

threshold = 128
binary_image = image.point(lambda p: p < threshold and 255)
contour = ladybug_contour(np.array(binary_image) == 0)  # Use True for black pixels

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Image")
plt.subplot(1, 2, 2)
plt.imshow(image, cmap='gray')

contour_x, contour_y = zip(*contour)

# отбелязвам само пикселите, които са контур без да ги свързвам
plt.scatter(contour_y, contour_x, color='purple', s=8)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Contour Pixels")
plt.show()
